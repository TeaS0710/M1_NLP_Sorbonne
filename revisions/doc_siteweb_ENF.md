Documentation du Site Web Intranet et de son Accès via Tunnel SSH
Introduction et Contexte

Ce document détaille l’architecture complète d’un site web hébergé sur un réseau privé (intranet), ainsi que les solutions mises en place pour le rendre accessible à distance de manière sécurisée. Le site web en question est initialement conçu pour une utilisation interne et n’est pas directement accessible depuis Internet. Afin de permettre un accès distant tout en conservant un environnement privé, nous avons mis en place un tunnel SSH pour rediriger le trafic web à travers un serveur intermédiaire. En termes simples, au lieu d’accéder directement au site à travers le réseau local, on emprunte un détour sécurisé via un serveur SSH distant
ionos.fr
. Cette technique de port forwarding permet justement de connecter un client à une machine qui n’a qu’une adresse IP privée derrière un routeur ou pare-feu
doc.fedora-fr.org
. Grâce à ce tunnel chiffré, les utilisateurs autorisés peuvent consulter le site web intranet depuis l’extérieur, comme s’ils étaient connectés au réseau local, tandis que les données échangées restent protégées via le protocole SSH.

Pile Technique et Architecture du Site

Serveur Intranet : Le site web est hébergé sur un serveur Linux au sein du réseau local privé (par exemple, un serveur Ubuntu ou Debian, ou encore un Raspberry Pi sous Raspbian). Ce serveur dispose d’une adresse IP privée (typiquement de la forme 192.168.x.x) et n’est pas directement joignable depuis Internet. Le site web tourne sur ce serveur intranet ; dans notre configuration, il est servi via un serveur HTTP Apache 2 (serveur web) écoutant sur le port 80, avec du contenu statique et dynamique en PHP. (On peut bien sûr adapter la pile logicielle : par exemple un serveur Nginx ou une application Node.js – l’important est que le service web écoute sur un port du serveur intranet, port 80 dans notre cas d’école.) Le serveur web est configuré pour démarrer automatiquement au boot du serveur intranet, assurant que le site est disponible sur le réseau local dès le démarrage.

Réseau Local (Intranet) : Le serveur intranet est connecté à un réseau privé (intranet) qui utilise des adresses IP privées (par exemple le sous-réseau 192.168.1.0/24). Seules les machines présentes sur ce réseau local peuvent accéder directement au site en utilisant l’URL interne (par exemple http://192.168.1.100 si le serveur a cette IP). Aucun port n’est exposé sur la passerelle Internet de ce réseau, de sorte que le site reste inaccessible depuis l’extérieur en l’absence de mécanisme spécifique (pas de redirection de port NAT statique configurée sur le routeur). Cette isolation garantit la confidentialité par défaut, mais nécessite une solution pour un accès à distance contrôlé – c’est le rôle du tunnel SSH décrit plus loin.

Serveur Passerelle SSH : Pour rendre le site accessible hors du réseau local, nous utilisons un second serveur, hébergé sur Internet (par exemple un VPS Linux) qui fera office de passerelle. Ce serveur possède une IP publique (ou un nom de domaine) et exécute un service SSH (OpenSSH). Il est configuré pour accepter les connexions SSH entrantes et servira de point d’ancrage pour le tunnel. Aucune application web n’est nécessaire sur ce serveur distant ; son rôle est simplement de récevoir la connexion SSH depuis le serveur intranet et d’ouvrir un port qui redirigera vers le site intranet.

Schéma d’ensemble : Le schéma ci-dessous illustre l’architecture : à gauche, le serveur intranet (réseau privé) hébergeant le site web et initiant un tunnel SSH sortant ; à droite, le serveur passerelle SSH (réseau public) qui termine le tunnel et rend le site accessible sur un port donné. Le trafic HTTP circule à l’intérieur du tunnel SSH sécurisé entre les deux serveurs.

Schéma du tunnel SSH (port forwarding distant) reliant le serveur intranet privé (gauche) au serveur passerelle public (droite). Le port 8080 sur le serveur distant est redirigé vers le port 80 du serveur intranet via la connexion SSH
superuser.com
.

Protocoles Utilisés

Plusieurs protocoles réseau entrent en jeu dans cette architecture :

HTTP (HyperText Transfer Protocol) : c’est le protocole utilisé par le site web lui-même pour communiquer les pages web. Le site tourne en HTTP sur le port 80 du serveur intranet. (Éventuellement, HTTP pourrait être encapsulé dans TLS pour du HTTPS, mais ici la confidentialité est déjà assurée par le tunnel SSH, nous sommes donc restés en HTTP interne pour simplifier.) Le trafic HTTP du site n’est pas accessible directement sur Internet, il circule uniquement soit localement dans l’intranet, soit à l’intérieur du tunnel SSH lorsqu’il sort vers l’extérieur.

SSH (Secure Shell) : c’est le protocole clé pour le tunnel. SSH fournit une connexion chiffrée entre deux hôtes et permet la redirection de port (aussi appelée tunneling). On utilise ici SSH en mode « tunnel inversé » (reverse port forwarding) : le client SSH est lancé depuis le serveur intranet (point A) vers le serveur passerelle (point B), et il demande à ouvrir un port sur B qui renverra vers A. Concrètement, lorsqu’on exécute la commande ssh -R, on dit au serveur SSH distant d’écouter sur un port donné et de renvoyer toute connexion reçue vers une adresse:port du côté client
doc.fedora-fr.org
. Ici, le serveur intranet ouvre un tunnel SSH vers la passerelle et demande l’ouverture du port distant (par ex. 8080) relié au port local 80 (le site web) : toute connexion arrivant sur le port 8080 de la passerelle est transmise via le tunnel SSH chiffré jusqu’au serveur intranet sur son port 80. On obtient ainsi l’effet d’un réseau privé virtuel : l’ordinateur distant peut accéder au site comme s’il était sur le LAN.

TCP/IP : Les deux protocoles ci-dessus s’appuient sur TCP/IP. Le tunnel SSH encapsule du trafic TCP (HTTP dans notre cas) au sein d’une connexion TCP chiffrée. Le serveur SSH distant écoute typiquement sur le port TCP 22 (port SSH par défaut) pour les connexions entrantes. Dans notre configuration, le serveur intranet initie une connexion TCP sortante vers l’adresse publique du serveur SSH (sur le port 22), ce qui traverse le NAT du routeur sans configuration spéciale (puisque le trafic est initié de l’intérieur vers l’extérieur). La connexion SSH établie, le port forwarding distant crée un socket TCP d’écoute sur le serveur passerelle (port 8080) et redirige les paquets vers l’intranet. Tout le flux de données HTTP est ainsi transporté au sein de la session SSH sur TCP/22.

En résumé, le site web utilise HTTP, et l’accès distant est rendu possible via SSH qui tunnelise ce flux HTTP. Le tout repose sur TCP/IP standard. L’utilisation d’SSH assure que la communication est chiffrée et authentifiée de bout en bout : la connexion empruntant Internet est illisible pour un tiers, seul le client SSH et le serveur SSH peuvent déchiffrer les données. La connexion est transparente pour l’utilisateur final et sécurisée via OpenSSH
doc.fedora-fr.org
.

Configuration du Réseau Privé Intranet

Dans l’implémentation réelle, le serveur intranet et le site web ont été configurés comme suit :

Adresse IP Locale : Le serveur intranet a une IP statique sur le réseau local (par exemple 192.168.1.100) afin que les autres machines de l’intranet puissent le joindre de façon fiable. L’usage d’une IP statique ou d’une réservation DHCP garantit que l’adresse ne change pas au fil du temps. Si le serveur utilise le Wi-Fi ou se déplace entre réseaux, il est important d’adapter la configuration (par exemple, un script de détection du réseau) ; dans notre cas, le serveur intranet reste généralement dans le même réseau local.

Accès Local au Site : Vérification est faite que le site est bien accessible depuis le LAN. Par exemple, depuis un PC du réseau, une requête vers http://192.168.1.100 (ou le nom DNS local s’il y en a un) renvoie la page d’accueil du site. Cette étape permet de s’assurer que le serveur web fonctionne correctement en interne avant de mettre en place le tunnel. Si un pare-feu local est activé sur le serveur intranet, il faut autoriser le port 80 en entrée pour le sous-réseau local.

Absence d’Accès Public Direct : Aucun port de ce serveur n’est exposé sur Internet via le routeur. Cela signifie que par défaut, depuis l’extérieur, il est impossible de se connecter à l’IP publique du réseau et d’atteindre le site. Ce cloisonnement assure que le site reste privé. L’ouverture d’accès se fera uniquement par le canal SSH sortant initié par le serveur intranet. (C’est une approche plus sécurisée que d’ouvrir le port 80 sur le routeur, car on évite d’exposer directement le service web et on bénéficie du chiffrement et de l’authentification SSH.)

En synthèse, le serveur intranet est prêt à fournir le service web sur son réseau privé, et aucune configuration de routage NAT n’est faite au niveau de la passerelle Internet. Cela prépare le terrain pour la mise en place du tunnel SSH qui va percer ce réseau privé de manière contrôlée.

Mise en Place du Tunnel SSH d’Accès Distant

Cette section décrit les étapes et configurations nécessaires pour créer le tunnel SSH permettant l’accès distant au site web. L’objectif est de faire en sorte que le port 8080 du serveur distant (passerelle) pointe vers le port 80 du serveur intranet, via une connexion SSH persistante initiée par le serveur intranet.

1. Création des Clés SSH pour l’Authentification

Pour automatiser et sécuriser la connexion SSH, on utilise une authentification par clé publique (plutôt qu’un mot de passe interactif). On génère donc une paire de clés SSH sur le serveur intranet :

# Sur le serveur intranet (en tant qu'utilisateur approprié, ex. "tunneluser")
ssh-keygen -t ed25519 -N "" -f ~/.ssh/id_tunnel


Cette commande crée une clé privée id_tunnel et une clé publique id_tunnel.pub dans ~/.ssh. Nous avons choisi l’algorithme Ed25519 (moderne et sécurisé par défaut), sans passphrase (-N "") pour permettre une utilisation automatisée (la clé privée non chiffrée sera protégée par les permissions du système et son accès restreint à l’utilisateur). On peut également utiliser RSA 4096 bits selon les besoins, mais Ed25519 est recommandé pour sa robustesse et sa compacité.

Ensuite, on doit installer la clé publique sur le serveur distant pour autoriser la connexion : on ajoute le contenu de id_tunnel.pub dans le fichier ~/.ssh/authorized_keys de l’utilisateur distant qui servira au tunnel. Par exemple, si on compte utiliser l’utilisateur tunnel sur la passerelle :

# Sur le serveur distant (passerelle SSH)
# (Supposons que l'utilisateur 'tunnel' existe déjà, sinon le créer)
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI...==" >> /home/tunnel/.ssh/authorized_keys
chmod 600 /home/tunnel/.ssh/authorized_keys
chown tunnel:tunnel /home/tunnel/.ssh/authorized_keys


(Remarque : on peut aussi utiliser la commande pratique ssh-copy-id, par ex. ssh-copy-id -i ~/.ssh/id_tunnel.pub tunnel@serveur-distant, pour transférer automatiquement la clé publique.)

Désormais, le serveur intranet pourra ouvrir une session SSH vers le serveur distant sans mot de passe, en utilisant sa clé privée. L’authentification par clés SSH utilise un chiffrement asymétrique et offre un haut niveau de sécurité
ionos.fr
 – seul le serveur intranet possédant la clé privée correspondante peut se connecter, et la clé privée ne quitte jamais la machine intranet.

2. Configuration du Serveur SSH Distant (Passerelle)

Sur le serveur distant, nous devons nous assurer que le service SSH (sshd) est configuré pour accepter le port forwarding distant vers l’extérieur. Deux points importants à vérifier/modifier dans /etc/ssh/sshd_config du serveur passerelle :

Autorisation du Port Forwarding : Par défaut, OpenSSH permet le tunneling (directive AllowTcpForwarding activée). Il convient de confirmer que AllowTcpForwarding est soit non présent (valeur par défaut “yes”), soit explicitement à “yes”. De même, s’assurer que PermitTunnel n’est pas restrictif (ce paramètre concerne surtout les tunnels niveau 2/3, pas le port forwarding classique, donc il peut rester par défaut).

Binding des Ports Distants (GatewayPorts) : Par défaut, les ports ouverts via ssh -R sur le serveur distant n’écoutent que sur l’interface loopback du serveur (adresse 127.0.0.1), ce qui limiterait l’accès du tunnel à la machine distante elle-même. Puisque nous souhaitons que le site soit accessible depuis n’importe quel client se connectant au serveur distant, nous devons autoriser l’écoute sur toutes les interfaces. Pour ce faire, on active GatewayPorts yes dans la configuration SSH du serveur distant
superuser.com
. On peut soit éditer sshd_config pour y ajouter la ligne : GatewayPorts yes, soit, plus ponctuellement, utiliser la syntaxe ssh -R 0.0.0.0:... côté client (serveur intranet) pour demander l’écoute sur 0.0.0.0. Important : même en utilisant 0.0.0.0 dans la commande, il faut que GatewayPorts soit à yes côté serveur pour que cette demande soit honorée. Après modification du fichier de configuration, on redémarre le service SSH sur le serveur distant (sudo systemctl restart sshd) pour appliquer les changements.

Firewall du Serveur Distant : Si un pare-feu (iptables/ufw) est actif sur la passerelle, il faut ouvrir le port choisi pour le tunnel (dans notre exemple, 8080 en TCP). Par exemple, avec UFW : sudo ufw allow 8080/tcp. Sans cela, même si sshd écoute, le port pourrait être bloqué au niveau du firewall. Veillez également à ce que le port 22 (ou le port custom SSH si changé) du serveur distant soit ouvert pour permettre la connexion SSH elle-même.

3. Commande de Tunnel SSH (Port Forwarding)

Avec la clé en place et le serveur distant configuré, nous pouvons établir manuellement le tunnel pour le tester. La commande SSH utilisée est la suivante (exécutée depuis le serveur intranet) :

ssh -N -R 0.0.0.0:8080:localhost:80 -i ~/.ssh/id_tunnel tunnel@serveur-distant.com


Explications des paramètres :

-N : indique de ne pas exécuter de commande distante (le SSH est utilisé uniquement pour le forwarding, pas pour ouvrir un shell).

-R 0.0.0.0:8080:localhost:80 : spécifie un tunnel Remote. Sur le serveur distant, le port 8080 (sur toutes les interfaces 0.0.0.0) sera ouvert. Toute connexion sur ce port sera transférée vers localhost:80 du côté du client (côté intranet). Ici localhost:80 s’entend depuis le serveur intranet (qui exécute la commande), ce qui correspond en fait à le site web local sur port 80. En somme, on relie le port 8080 distant au port 80 local.

-i ~/.ssh/id_tunnel : option pour spécifier la clé privée à utiliser (notre clé sans passphrase générée plus haut). Ceci permet de s’assurer qu’on utilise la bonne clé et d’automatiser la connexion sans demande de mot de passe.

tunnel@serveur-distant.com : c’est l’utilisateur (tunnel) et l’adresse (ou IP) du serveur SSH distant. Il faut bien entendu remplacer par le bon nom de domaine ou IP publique de votre passerelle SSH.

Après avoir lancé cette commande, si tout est correct, il ne se passe rien d’apparent (puisqu’on a -N et pas de shell ouvert) : c’est normal. Le tunnel est désormais établi en arrière-plan tant que la session SSH reste ouverte. Sur le serveur distant, le port 8080 est en écoute. On peut vérifier côté distant, par exemple via ss -tnlp | grep 8080 (ou netstat -anp) que sshd écoute sur 0.0.0.0:8080.

Test du tunnel : À ce stade, on teste l’accès au site via le tunnel. Depuis une machine extérieure (n’importe quel poste ayant accès à Internet, par exemple votre ordinateur personnel hors du réseau intranet), on tente d’atteindre le site en ouvrant http://<adresse_du_serveur_distant>:8080 dans un navigateur. L’adresse du serveur distant peut être son IP publique (par ex. http://203.0.113.10:8080) ou un nom DNS pointant vers lui. On devrait voir s’afficher le site web intranet comme si on était en local. Autrement dit, le serveur distant agit comme un relais : il transmet la requête reçue sur son port 8080 à travers le tunnel SSH jusqu’au serveur intranet, qui répond avec la page web, renvoyée par le même chemin.

Si le contenu du site s’affiche correctement via cette URL externe, cela confirme que le port forwarding SSH fonctionne. À ce stade, nous avons donc une solution technique opérationnelle : le site intranet est accessible à distance à travers un tunnel SSH sécurisé, tout en n’étant pas exposé directement sur Internet (seul le port SSH de la passerelle est ouvert publiquement). Notez que toute personne connaissant l’URL (IP:8080) pourrait en théorie accéder au site pendant que le tunnel est levé, puisqu’on a permis l’écoute sur 0.0.0.0 (toutes interfaces). Si l’application web nécessite une restriction d’accès supplémentaire, on pourrait filtrer par adresse IP ou mettre en place une authentification au niveau de l’application. Dans notre cas, le site n’exposant pas de données sensibles sans authentification utilisateur, cette exposition contrôlée est acceptable. De plus, le tunnel n’est pas permanent pour l’instant (juste un test manuel) et nous allons voir comment le rendre persistant de manière maîtrisée.

4. Automatisation du Tunnel SSH (Service au Démarrage)

Pour que le site soit effectivement accessible en permanence via le tunnel, il faut que ce dernier soit établi automatiquement au démarrage du serveur intranet, et qu’il se rétablisse en cas de coupure. Nous avons mis en place deux éléments complémentaires : l’utilisation de AutoSSH pour maintenir la connexion, et un script/servive système pour lancer le tunnel au boot et lors des changements de réseau.

Installation de AutoSSH : AutoSSH est un outil qui surveille une session SSH et la redémarre automatiquement si elle se coupe ou gèle. On l’installe sur le serveur intranet :

sudo apt update && sudo apt install autossh


Une fois installé, on peut tester la même commande de tunnel via autossh. La syntaxe de base est similaire, par exemple :

autossh -M 0 -N -R 0.0.0.0:8080:localhost:80 -i ~/.ssh/id_tunnel tunnel@serveur-distant.com


Explication : l’option -M 0 désactive le mode surveillance par port séparé (on utilise les mécanismes de keepalive à la place), autossh va relancer ssh s’il détecte la fin anormale du tunnel. En pratique, autossh permet de conserver le tunnel ouvert de façon persistante, même en cas de micro-coupure réseau ou de redémarrage du service SSH distant. Si le processus SSH se termine, autossh le relance automatiquement
superuser.com
.

Service système (systemd) : Pour le démarrage automatique, on crée un service systemd dédié sur le serveur intranet. Voici un exemple de fichier /etc/systemd/system/tunnel.service que nous avons utilisé :

<details><summary><code>/etc/systemd/system/tunnel.service</code></summary><pre><code>[Unit] Description=Tunnel SSH reverse pour exposer le site intranet After=network-online.target Wants=network-online.target

[Service]
User=tunneluser # utilisateur local exécutant le tunnel
ExecStart=/usr/bin/ssh -NT -o ServerAliveInterval=60 -o ServerAliveCountMax=3 -i /home/tunneluser/.ssh/id_tunnel -R 0.0.0.0:8080:localhost:80 tunnel@serveur-distant.com
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
</code></pre></details>

Dans ce service, on a choisi d’utiliser directement le binaire ssh avec des options de keepalive au lieu d’autossh pour montrer les deux approches (on aurait pu écrire ExecStart=/usr/bin/autossh ... de manière équivalente). Quelques points à noter :

Dépendance réseau : After=network-online.target s’assure que le script attend que la couche réseau soit pleinement opérationnelle au démarrage avant d’établir le tunnel. Ceci évite le problème où le service SSH serait lancé trop tôt (avant obtention d’une IP via DHCP par exemple) et échouerait. On associe aussi Wants=network-online.target pour forcer l’activation du service de surveillance du réseau.

Utilisateur : on spécifie User=tunneluser (adapté à votre cas) pour exécuter le tunnel avec un compte non privilégié dédié, plutôt qu’avec root, pour des raisons de sécurité (ce compte doit avoir accès à la clé privée et aux commandes SSH).

Commande : on retrouve la commande ssh -N -R ... discutée précédemment. S’y ajoutent deux options -o très importantes :

ServerAliveInterval=60 et ServerAliveCountMax=3 configurent des keep-alive SSH côté client
superuser.com
. Concrètement, le client enverra un paquet vide toutes les 60s et considérera la connexion perdue au bout de 3 échecs consécutifs (soit environ 3 minutes sans réponse). Ces paramètres permettent de détecter rapidement une coupure de connexion (par exemple si la connexion Internet tombe ou si l’IP change) plutôt que d’attendre le délai TCP par défaut qui peut être très long. Ainsi, si le serveur intranet change de réseau ou si la session devient non fonctionnelle, le client SSH s’en rendra compte et se terminera au bout de ~180s d’inactivité non répondue. Couplé à Restart=always, cela provoquera une relance automatique du tunnel.

L’option -o ExitOnForwardFailure=yes pourrait également être ajoutée pour faire en sorte que si l’établissement du port forward distant échoue (par ex. si le port 8080 est déjà pris sur le serveur distant), alors SSH se termine immédiatement. Dans notre cas, ce n’est pas strictement nécessaire car nous contrôlons le port utilisé et on souhaite de toute façon que le service redémarre même en cas d’échec initial.

Redémarrage automatique : Restart=always avec RestartSec=10 signifie que si le processus (ssh) se termine ou échoue, systemd attend 10 secondes puis le relance. Cela garantit la persistance du tunnel. Couplé aux keep-alive, dès qu’une coupure est détectée et que ssh se ferme, le service le relancera, essayant indéfiniment de rétablir la connexion.

On enregistre ce fichier, puis on active le service :

sudo systemctl daemon-reload
sudo systemctl enable tunnel.service
sudo systemctl start tunnel.service


Le tunnel SSH va alors s’établir automatiquement en arrière-plan. En cas de redémarrage du serveur intranet, systemd relancera le service au boot (grâce à l’enable). En cas d’échec de connexion (par ex. serveur distant injoignable), le service tentera en boucle avec un délai, jusqu’à réussir.

5. Gestion des Clés et Sécurité des Connexions

La sécurité de l’ensemble repose sur SSH, il est donc crucial de gérer correctement les clés et la confiance entre les machines :

Authentification par clé privée/publique : Comme vu, seul le serveur intranet disposant de la clé privée appropriée peut ouvrir le tunnel vers le serveur distant. La clé privée est stockée de façon sécurisée (~/.ssh/id_tunnel avec permissions 600). La clé publique correspondante est installée sur le serveur distant dans authorized_keys de l’utilisateur tunnel. Il est recommandé de restreindre les droits associés à cette clé dans le fichier authorized_keys pour plus de sûreté. Par exemple, on peut préfixer la ligne par from= pour limiter l’adresse source autorisée (si l’IP du serveur intranet est plus ou moins fixe), ou encore utiliser l’option command="echo 'port forwarding only'" combinée à no-pty,no-X11-forwarding etc., bien que dans notre cas on a besoin du port forwarding. Dans une configuration avancée, on pourrait créer une clé dédiée avec des restrictions pour qu’elle ne puisse servir qu’à cet usage précis du tunnel.

Confidentialité du tunnel : Toutes les données qui transitent entre le serveur intranet et le serveur distant sont chiffrées par SSH. On profite de l’algorithme de chiffrement robuste (AES, ChaCha20, etc. négocié par SSH) et de l’échange de clés sécurisé. Ainsi, même si le site web lui-même n’utilise pas HTTPS en interne, le fait de passer par le tunnel SSH assure qu’en sortie du serveur intranet jusqu’à l’arrivée sur le serveur distant, tout est crypté. La connexion empruntant Internet est donc sécurisée et ne peut être espionnée en clair, assurant l’intégrité et la confidentialité des échanges
doc.fedora-fr.org
.

Authenticité du serveur distant (Empreinte SHA-256) : Lors de la première connexion SSH, le client (serveur intranet) doit vérifier l’empreinte de la clé hôte du serveur distant. SSH affiche un message du type : “The authenticity of host ‘serveur-distant.com (xx.xx.xx.xx)’ can’t be established... RSA/ECDSA/ED25519 key fingerprint is SHA256:.... Cette empreinte SHA256 est un condensé de la clé publique du serveur distant
superuser.com
. Nous avons comparé cette empreinte avec celle fournie par l’administrateur (ou affichée par un autre moyen sûr) pour nous assurer que nous nous connectons bien au bon serveur (prévention des attaques de type man-in-the-middle). Une fois la confiance établie, on a répondu "yes" pour ajouter la clé du serveur distant dans le fichier ~/.ssh/known_hosts du serveur intranet. À l’avenir, chaque connexion SSH vérifiera que la clé du serveur correspond à cette entrée connue, garantissant l’authenticité du serveur.

Astuce : Dans un contexte automatisé (service systemd), l’acceptation interactive de la clé hôte n’est pas possible. Il fallait donc gérer ce point. Deux approches sont possibles : soit pré-remplir le known_hosts manuellement avec la clé hôte du serveur distant (par exemple en utilisant la commande ssh-keyscan -H serveur-distant.com >> ~/.ssh/known_hosts depuis le serveur intranet), soit configurer SSH pour qu’il n’attende pas la confirmation. Pour la simplicité, nous avons temporairement utilisé l’option -o StrictHostKeyChecking=no lors du premier test, afin d’accepter automatiquement la clé hôte non reconnue. Cependant, pour la solution pérenne, la clé hôte a été ajoutée au known_hosts afin que StrictHostKeyChecking puisse rester à yes (valeur par défaut sécurisée). De cette façon, notre service auto démarre sans encombre et sans compromis de sécurité.

Limitation de l’accès au site : Comme mentionné plus haut, ouvrir le port 8080 sur 0.0.0.0 du serveur distant rend le site accessible à toute adresse IP connaissant ce port. Dans notre cas d’usage, cela était acceptable (site de test/démo). Si l’on souhaitait restreindre davantage l’accès, on pourrait :

Utiliser un bind sur localhost uniquement (ne pas mettre 0.0.0.0 et laisser GatewayPorts no), puis se connecter en SSH au serveur distant pour effectuer un port forward local supplémentaire. Cette solution est plus contraignante pour l’accès (double tunnel SSH en quelque sorte) et était inutile pour nous.

Ou plus simplement, laisser 0.0.0.0 mais configurer le pare-feu du serveur distant pour n’accepter des connexions sur le port 8080 que depuis certaines adresses IP de confiance.

Une autre alternative aurait été de mettre en place un VPN complet entre l’extérieur et l’intranet, mais cela ajoutait de la complexité. Le tunnel SSH répond au besoin avec légèreté et sécurité.

En suivant ces bonnes pratiques, le tunnel SSH offre un accès distant sécurisé et maîtrisé au site intranet. Les clés SSH asymétriques assurent l’authentification forte des machines
ionos.fr
, et le chiffrement protège les données en transit.

Comportement au Démarrage et lors des Changements de Réseau

Une fois la configuration mise en place, voici le comportement attendu du système, tant au démarrage du serveur intranet qu’en cas de modifications de connectivité :

Au démarrage du serveur intranet : Le service systemd tunnel.service se lance automatiquement. Il attend que le réseau soit en ligne, puis exécute la commande SSH (via autossh ou ssh direct). Quelques secondes après le boot, le tunnel SSH est établi vers la passerelle. En parallèle, le serveur web Apache s’est lancé (souvent bien avant, car Apache démarre dès que le système multi-user est up, même si le timing exact importe peu). Ainsi, dès que le tunnel est actif, le site est accessible via le serveur distant. Dans les journaux (sudo journalctl -u tunnel.service), on devrait voir la connexion s’établir. S’il y a un problème (ex: clé non acceptée, pas de réseau, DNS indisponible), le service va réessayer automatiquement grâce à Restart=always.

En fonctionnement normal : Pendant que le serveur intranet reste allumé et connecté, le tunnel reste levé en permanence. La consommation de ressources du tunnel SSH est minime (quelques Mo de RAM, CPU négligeable, bande passante uniquement en cas de trafic HTTP). Régulièrement (toutes les 60 secondes dans notre config), le client SSH envoie un paquet keepalive vers le serveur distant. Si tout va bien, il reçoit une réponse et rien ne se passe de plus. Ce mécanisme maintient la session vivante à travers certains pare-feux/routeurs qui pourraient sinon fermer une connexion inerte, et surveille l’état de la connexion.

En cas de coupure réseau ou de changement d’adresse IP : Si le serveur intranet perd la connectivité (exemple : câble débranché, Wi-Fi déconnecté, box Internet en panne) ou change de réseau (exemple : déplacement du serveur ou changement de point d’accès), le tunnel SSH va inévitablement se rompre. Grâce aux paramètres de keepalive, le client SSH détectera l’absence de réponse après 3 tentatives infructueuses (~3 minutes) et conclura que la session n’est plus valide, ce qui provoquera la terminaison du processus SSH
superuser.com
. Immédiatement, systemd (ou autossh) va tenter de relancer la connexion (RestartSec=10 assure une petite attente de 10s avant retry, ce qui évite de surcharger en cas de panne prolongée). Une fois que le réseau revient et que le serveur distant redevient joignable (par exemple, le serveur intranet obtient une nouvelle IP et retrouve l’accès Internet), la prochaine tentative de connexion SSH réussit et le tunnel est rétabli automatiquement. Du point de vue des utilisateurs extérieurs, le site peut sembler indisponible pendant la période de coupure, mais il redevient accessible dès que le serveur intranet est de nouveau en ligne et que le tunnel s’est reconnecté. Il n’y a pas besoin d’intervention manuelle.

Disponibilité du site via la passerelle : Tant que le tunnel est actif, le site est accessible à l’adresse http://serveur-distant:8080. Si le serveur intranet redémarre, il faudra le temps qu’il boote et remonte le tunnel (quelques dizaines de secondes) pour que l’accès revienne. Si le serveur distant (passerelle) redémarre, la session SSH sera évidemment coupée et le client intranet tentera de se reconnecter jusqu’à réussite. On a donc une robustesse acceptable dans la plupart des cas d’usage. Pour surveiller le bon fonctionnement en production, on pourrait mettre en place un petit script de monitoring qui teste régulièrement l’URL distante et envoie une alerte en cas d’inaccessibilité prolongée, mais ce n’était pas explicitement requis dans notre contexte.

Problèmes Rencontrés et Solutions Apportées

Durant la mise en place de cette infrastructure, nous avons rencontré plusieurs difficultés techniques, que nous avons résolues comme suit :

Acceptation de la Clé Hôte SSH (empreinte non connue) : Au premier essai du tunnel, la session SSH s’est bloquée en attente d’une confirmation manuelle de la clé du serveur distant (message « The authenticity of host ... can’t be established... Are you sure you want to continue connecting (yes/no)? »). Ce comportement de sécurité par défaut empêchait l’automatisation. Pour y remédier, nous avons, dans un premier temps, exécuté manuellement une connexion SSH vers le serveur distant afin d’enregistrer sa clé dans known_hosts. L’empreinte SHA256 affichée a été vérifiée puis acceptée, ajoutant ainsi l’entrée correspondante
superuser.com
. Par la suite, plus de blocage interactif : le service a pu se connecter directement. (En alternative, comme évoqué plus haut, l’option StrictHostKeyChecking=no a été testée lors du débogage initial pour forcer l’acceptation, mais ce n’est pas laissé en production par prudence.)

Horodatage et fuseau horaire : Un détail mineur rencontré, le serveur distant était en UTC tandis que le serveur local en heure locale, ce qui compliquait la corrélation des logs. Nous avons harmonisé les fuseaux ou pris en compte ce décalage lors de l’analyse des journaux. Ce point n’impacte pas le fonctionnement, mais est utile pour interpréter correctement les événements d’un côté et de l’autre.

Démarrage du tunnel trop précoce : Initialement, nous avions configuré le service avec After=network.target. Cependant, il arrivait que le tunnel tente de se connecter avant que l’adresse IP ne soit obtenue via DHCP, menant à un échec immédiat. La solution a été de modifier l’unité systemd pour cibler network-online.target et ajouter une petite temporisation (nous avons opté pour la relance automatique plutôt qu’un ExecStartPre=/bin/sleep 15 par exemple, afin de ne pas retarder inutilement quand le réseau est prêt). Après ce correctif, le tunnel se lève de manière fiable au boot.

Maintien du tunnel en cas d’inactivité : Sans configuration particulière, on a constaté que le tunnel pouvait se fermer au bout d’un certain temps d’inactivité (selon les politiques NAT de l’opérateur ou d’autres facteurs). Pour éviter cela, nous avons introduit les keep-alive SSH (ServerAliveInterval & ServerAliveCountMax) comme détaillé plus haut. Ces messages périodiques empêchent la session de stagner complètement et évitent les timeouts silencieux. Depuis ce changement, le tunnel reste indéfiniment actif, même en l’absence de trafic HTTP utilisateur, ce qui était l’effet recherché.

Choix du port distant déjà utilisé : Nous avons initialement tenté d’utiliser le port 80 sur le serveur distant pour accéder au site sans préciser de port (ex: http://serveur-distant/ au lieu de :8080). Cela nécessitait que le processus SSH sur le serveur distant puisse écouter le port 80, ce qui implique des privilèges root sur ce serveur (ports <1024). Par mesure de simplicité et de sécurité, nous avons renoncé à cette idée et choisi un port non privilégié (8080) pour le tunnel, afin de pouvoir utiliser un compte non-root et éviter tout conflit avec le serveur web éventuel du VPS. Si vraiment un port 80 ou 443 était requis (par exemple pour un public plus large ne devant pas entrer :8080), on aurait pu configurer sur le serveur distant un proxy (nginx ou iptables redirigeant 80 vers 8080) ou effectuer la connexion SSH en tant que root. Mais ce n’était pas nécessaire dans notre contexte.

Permissions du compte utilisateur tunnel : Le compte tunneluser sur le serveur intranet devait posséder les droits suffisants pour lancer la commande SSH au démarrage. Nous avons dû veiller à ce qu’il ait accès à la clé privée (~/.ssh/id_tunnel avec les bonnes permissions). De plus, comme ce compte initie la connexion, il doit pouvoir résoudre le nom de domaine du serveur distant (nécessite que le service DNS soit opérationnel au moment du démarrage du tunnel). En cas d’échecs de résolution DNS observés, on pourrait ajouter ExecStartPre=/usr/bin/getent hosts serveur-distant.com pour forcer la résolution ou utiliser l’adresse IP directement dans la commande SSH pour éliminer le facteur DNS. Nous n’avons pas eu de souci de DNS dans notre cas, le résolveur local étant disponible rapidement.

Diagnostics en cas de problème : Pour faciliter le débogage lors de la mise en place, nous avons temporairement ajouté l’option -v (verbose) à la commande SSH pour obtenir des informations détaillées dans les logs systemd. Cela a permis d’identifier rapidement les étapes où ça coinçait (par exemple l’échange de clés, ou l’attente de réseau). Une fois stable, nous avons retiré ce mode verbeux pour éviter des logs verbeux en continu.

Chaque problème rencontré a donc été résolu par une configuration appropriée ou un ajustement de script. La documentation ci-dessus intègre toutes ces solutions afin qu’une personne reprenant ce projet puisse éviter ces écueils et directement bénéficier d’un setup fonctionnel.

Conclusion

En suivant ce guide, il est possible de recréer intégralement le même environnement et les mêmes outils à l’avenir. Nous avons couvert : la pile technique du site web (système, serveur web, réseau intranet), la mise en place d’un tunnel SSH inversé pour exposer un service interne, l’automatisation du tunnel au démarrage du système, ainsi que les considérations de sécurité (clés SSH, chiffrement) et la gestion des problèmes rencontrés (startup ordering, maintien de la connexion, etc.). Les commandes précises, configurations de fichiers et explications protocolaires fournies dans ce document constituent une référence complète pour déployer une solution d’accès distant sécurisé à un site intranet. Grâce à l’implémentation du tunnel SSH, les tunnels SSH permettent d’accéder à des sites non disponibles depuis un réseau local en passant par un serveur intermédiaire
ionos.fr
, tout en maintenant un haut niveau de sécurité et de contrôle. L’ensemble de la connexion s’effectue de manière chiffrée et authentifiée, assurant que seules les personnes autorisées peuvent accéder aux ressources internes, et ce de façon transparente.

Cette documentation complète peut servir de modèle pour des projets similaires alliant réseau privé et accès distant ; elle doit permettre à un administrateur de reproduire étape par étape la configuration, ou de l’adapter en fonction de besoins voisins, avec tous les détails requis pour comprendre et maîtriser le fonctionnement de bout en bout. En cas d’évolution (par exemple changement de serveur distant, ajout d’un second port à forwarder, etc.), les principes exposés ici demeurent applicables et pourront être étendus. Nous disposons ainsi d’une solution robuste pour accéder à notre site intranet en mobilité, sans compromettre la sécurité ni la confidentialité des données transmises.

```bash
0) Prérequis (serveur & clients)
# Serveur (Ubuntu)
sudo apt update
sudo apt install -y openssh-server fail2ban ufw python3

# Client (Ubuntu/KDE…)
sudo apt update
sudo apt install -y openssh-client autossh sshfs jq curl

1) Serveur : SSH + pare-feu + intranet
# SSH écoute sur 2222, pas de mot de passe (pubkey only)
sudo sed -i \
  -e 's/^#\?Port .*/Port 2222/' \
  -e 's/^#\?PasswordAuthentication .*/PasswordAuthentication no/' \
  -e 's/^#\?PubkeyAuthentication .*/PubkeyAuthentication yes/' \
  -e '/^AllowUsers /d;$a AllowUsers teas' \
  -e '/^AllowTcpForwarding /d;$a AllowTcpForwarding yes' \
  /etc/ssh/sshd_config
sudo systemctl restart ssh

# UFW : n’ouvrir que 2222/tcp
sudo ufw allow 2222/tcp
sudo ufw --force enable
sudo ufw status

# Fail2Ban de base (sshd)
sudo systemctl enable --now fail2ban
sudo fail2ban-client status sshd

# Intranet en loopback (127.0.0.1:8000)
sudo tee /etc/systemd/system/intranet.service >/dev/null <<'EOF'
[Unit]
Description=Intranet Dashboard (loopback)
After=network.target

[Service]
User=teas
WorkingDirectory=/home/teas/intranet-dashboard
ExecStart=/usr/bin/python3 /home/teas/intranet-dashboard/server.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable --now intranet.service
sudo ss -tuln | grep '127.0.0.1:8000'     # doit lister 127.0.0.1:8000

2) Client : clés, alias SSH, tunnel, SSHFS
# Clé dédiée au tunnel (SANS passphrase)
ssh-keygen -t ed25519 -N "" -f ~/.ssh/id_ed25519_tunnel -C tunnel-intranet

# Déposer la clé sur le serveur (via FQDN ou IP)
ssh-copy-id -i ~/.ssh/id_ed25519_tunnel.pub -p 2222 teas@monserveur.dyndns.org
# (ou)
ssh-copy-id -i ~/.ssh/id_ed25519_tunnel.pub -p 2222 teas@89.80.61.108

# Alias SSH pratique : ~/.ssh/config
mkdir -p ~/.ssh && chmod 700 ~/.ssh
cat >> ~/.ssh/config <<'EOF'

Host cloud
  HostName monserveur.dyndns.org
  Port 2222
  User teas
  IdentityFile ~/.ssh/id_ed25519_tunnel
  ServerAliveInterval 15
  ServerAliveCountMax 3
  ExitOnForwardFailure yes
EOF
chmod 600 ~/.ssh/config

2.1 Tunnel + site
# Tunnel 8080 → (cloud)127.0.0.1:8000
ssh -f -N -L 8080:127.0.0.1:8000 cloud

# Test HTTP
curl -I http://127.0.0.1:8080/ | head -n1      # HTTP/1.0 200 OK attendu

2.2 Partage SSHFS
mkdir -p ~/ServeurShare
sshfs -o reconnect cloud:/home/teas/SharedFiles ~/ServeurShare
mount | grep ServeurShare                       # vérif

3) Démarrage automatique (systemd-user)
3.1 Tunnel (version SSH simple)
mkdir -p ~/.config/systemd/user
tee ~/.config/systemd/user/intranet-tunnel.service >/dev/null <<'EOF'
[Unit]
Description=Tunnel SSH 8080→127.0.0.1:8000 (auto)
After=network-online.target

[Service]
ExecStartPre=/bin/bash -c 'ss -ln | grep -q ":8080 " && fuser -k 8080/tcp || true'
ExecStart=/usr/bin/ssh -NT -L 8080:127.0.0.1:8000 cloud
Restart=always
RestartSec=5
StartLimitIntervalSec=0

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload
loginctl enable-linger "$USER"
systemctl --user enable --now intranet-tunnel.service
systemctl --user status intranet-tunnel --no-pager

3.2 Tunnel (version autossh – plus robuste en itinérance)
tee ~/.config/systemd/user/intranet-tunnel.service >/dev/null <<'EOF'
[Unit]
Description=Tunnel autossh 8080→127.0.0.1:8000 (cloud)
After=network-online.target

[Service]
Environment=AUTOSSH_GATETIME=0
ExecStartPre=/bin/bash -c 'ss -ln | grep -q ":8080 " && fuser -k 8080/tcp || true'
ExecStart=/usr/bin/autossh -M 0 -NT -L 8080:127.0.0.1:8000 cloud
Restart=always
RestartSec=5
StartLimitIntervalSec=0

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload
systemctl --user enable --now intranet-tunnel.service

3.3 SSHFS auto
tee ~/.config/systemd/user/sshfs-share.service >/dev/null <<'EOF'
[Unit]
Description=Montage SSHFS cloud perso
After=network-online.target intranet-tunnel.service
Wants=intranet-tunnel.service

[Service]
ExecStartPre=/usr/bin/mkdir -p %h/ServeurShare
ExecStart=/usr/bin/sshfs -f -o reconnect cloud:/home/teas/SharedFiles %h/ServeurShare
ExecStop=/bin/fusermount -u %h/ServeurShare
Restart=always
RestartSec=5

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload
systemctl --user enable --now sshfs-share.service

4) Autostart avec anti-doublon (ouvre le site au login)
mkdir -p ~/.local/bin
tee ~/.local/bin/open_intranet.sh >/dev/null <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
URL="http://127.0.0.1:8080/"

mkdir -p ~/.cache
exec 9>~/.cache/open_intranet.lock
flock -n 9 || exit 0

if ! ss -ln | grep -q ':8080 '; then
  systemctl --user start intranet-tunnel.service || true
  for i in {1..10}; do ss -ln | grep -q ':8080 ' && break || sleep 1; done
fi

for i in {1..10}; do curl -fsS --max-time 1 "$URL" >/dev/null && break || sleep 1; done

pgrep -af "127.0.0.1:8080" >/dev/null && exit 0
xdg-open "$URL" >/dev/null 2>&1 &
disown
EOF
chmod +x ~/.local/bin/open_intranet.sh

mkdir -p ~/.config/autostart
tee ~/.config/autostart/intranet.desktop >/dev/null <<'EOF'
[Desktop Entry]
Type=Application
Name=Intranet Dashboard
Comment=Ouvre l’intranet local (anti-doublon)
Exec=/home/teas/.local/bin/open_intranet.sh
Icon=folder-remote
Terminal=false
X-GNOME-Autostart-Delay=8
X-KDE-autostart-after=panel
EOF


(désactive tes anciens .desktop doublons en les renommant .disabled si besoin)

5) Vérifications rapides (client)
ss -ln | grep ':8080 '                          # écoute tunnel
mount | grep ServeurShare                       # SSHFS monté
curl -s --max-time 3 http://127.0.0.1:8080/metrics | jq

6) Vérifications serveur
sudo ss -tuln | grep ':2222 '                   # SSH exposé
sudo ss -tuln | grep '127.0.0.1:8000'           # intranet loopback
sudo systemctl status intranet.service --no-pager
sudo journalctl -u intranet.service -n 50 --no-pager
sudo fail2ban-client status sshd

7) Bascule/itinérance réseau (robustesse)
# Option 1 (recommandée) : autossh (déjà configuré ci-dessus)
systemctl --user restart intranet-tunnel

# Option 2 (SSH simple) : relance “à la main”
pkill -f "ssh .*8080:127.0.0.1:8000" || true
ssh -f -N -L 8080:127.0.0.1:8000 cloud

8) Audit « pas de fuite » (client)
echo "=== ports non loopback ==="; ss -tuln4 | awk '$4 !~ /^127/ && NR>1{print}'
echo "=== tunnel ==="; ss -ln | grep ':8080 ' && echo OK || echo KO
echo "=== sshfs ==="; mount | grep ServeurShare && echo OK || echo KO
echo "=== site ==="; curl -s --max-time 3 http://127.0.0.1:8080/ >/dev/null && echo OK || echo KO

9) Fail2Ban depuis le client
# Voir si ton IP publique est bannie
MYIP=$(curl -s https://ifconfig.me)
ssh cloud "sudo fail2ban-client exec sshd banned" | grep -q "$MYIP" \
  && echo "$MYIP bannie" || echo "$MYIP OK"

# Débannir une IP précise
IP="203.0.113.42"
ssh cloud "sudo fail2ban-client set sshd unbanip $IP"

10) Dépannage express
# “Address already in use” sur 8080 → tuer l’ancien tunnel
pkill -f "ssh .*8080:127.0.0.1:8000" || true
fuser -k 8080/tcp 2>/dev/null || true

# “Permission denied (publickey)” → clé absente/chemin faux
ssh -i ~/.ssh/id_ed25519_tunnel -p 2222 teas@monserveur.dyndns.org 'echo auth OK'
# si KO : copier la clé
ssh-copy-id -i ~/.ssh/id_ed25519_tunnel.pub -p 2222 teas@monserveur.dyndns.org

# Relancer services user
systemctl --user daemon-reload
systemctl --user restart intranet-tunnel sshfs-share
systemctl --user status intranet-tunnel sshfs-share --no-pager

11) Scripts d’audit (optionnel)
# Serveur
sudo tee /usr/local/bin/audit_server.sh >/dev/null <<'EOF'
#!/usr/bin/env bash
echo "=== Server audit $(date)"
sudo ss -tuln | awk '/:2222/ {p++} END{print (p?"Port 2222 OK":"Port 2222 ABSENT")}'
sudo ss -tuln | awk '/:8000/ && /127.0.0.1/ {l++} END{print (l?"Loopback 8000 OK":"8000 exposé !")}'
sudo fail2ban-client status sshd | awk '/Currently banned/ {print}'
sudo journalctl -u intranet.service -n 10 --no-pager | grep -qi error && echo "Erreurs intranet !" || echo "Intranet clean"
df -h / | awk 'NR==2 {print "Disk root "$5}'
EOF
sudo chmod +x /usr/local/bin/audit_server.sh

# Client
tee ~/audit.sh >/dev/null <<'EOF'
#!/usr/bin/env bash
echo "=== Client audit $(date)"
ss -tuln4 | awk '$4 !~ /^127/ && NR>1 {print $0}' || echo "✓ Aucun port exposé"
ss -ln | grep ':8080 ' && echo "✓ Tunnel 8080 actif" || echo "✗ Tunnel absent"
mount | grep ServeurShare && echo "✓ SSHFS monté" || echo "✗ SSHFS manquant"
curl -s --max-time 3 http://127.0.0.1:8080/metrics >/dev/null && echo "✓ Intranet répond" || echo "✗ Intranet KO"
EOF
chmod +x ~/audit.sh

12) Nettoyage autostarts doublons (si page qui s’ouvre deux fois)
cd ~/.config/autostart
ls -1
mv -v intranet-chrome.desktop{,.disabled} 2>/dev/null || true
mv -v intranet-dashboard.desktop{,.disabled} 2>/dev/null || true
grep -RIn '^Exec=' .

Résumé d’usage

Accéder au site : http://127.0.0.1:8080

Monter le cloud : ~/ServeurShare

Tout redémarrer (client) : systemctl --user restart intranet-tunnel sshfs-share

Audit rapide (client) : ~/audit.sh

Audit serveur : /usr/local/bin/audit_server.sh
```
