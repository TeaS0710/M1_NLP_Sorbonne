### serveur

sftp://teas@89.80.61.108:2222/home/teas/SharedFiles

# Terminal (Konsole)
sshfs -p 2222 teas@89.80.61.108:/home/teas/SharedFiles  ~/ServeurShare

# remonte s’il était arrêté
systemctl --user restart sshfs-share.service

# ou simplement : start (si l’état est inactive)
systemctl --user start sshfs-share.service

ln -sf ~/ServeurShare ~/Serveur


# Mises à jour
sudo apt update && sudo apt upgrade -y

# Paquets indispensables
sudo apt install openssh-server ufw fail2ban -y

# Ici l’utilisateur choisi est « teas » (déjà existant)
sudo passwd teas         # définir ou changer le mot de passe

sudo nano /etc/ssh/sshd_config

Port 2222
PermitRootLogin no
PasswordAuthentication no          # ← remis plus tard à yes puis de nouveau no
KbdInteractiveAuthentication no
PubkeyAuthentication yes
AllowUsers teas
UsePAM yes

---
sudo systemctl disable --now ssh.socket
sudo systemctl mask ssh.socket
sudo systemctl enable --now ssh.service

sudo ufw allow 2222/tcp
sudo ufw delete allow 22/tcp    # si la règle existait
sudo ufw enable

sudo ss -tulnp | grep ssh           # doit écouter sur :2222
sudo sshd -T | grep -i port         # doit afficher port 2222

mkdir -p ~/.ssh && chmod 700 ~/.ssh
ssh-keygen -t ed25519 -C "pc-fixe"   # ↵ ↵ ↵ (chemin par défaut, passphrase optionnelle)

ssh-copy-id -p 2222 -i ~/.ssh/id_ed25519.pub teas@89.80.61.108
# → Permission denied (publickey)

sudo nano /etc/ssh/sshd_config
# PasswordAuthentication yes
# KbdInteractiveAuthentication yes
sudo systemctl restart ssh

ssh-copy-id -p 2222 -i ~/.ssh/id_ed25519.pub teas@89.80.61.108

ssh -p 2222 teas@89.80.61.108       # plus de mot de passe demandé

sudo nano /etc/ssh/sshd_config
# PasswordAuthentication no
# KbdInteractiveAuthentication no
sudo systemctl restart ssh

# Vérifier options actives
sudo sshd -T | grep -E 'passwordauthentication|kbdinteractiveauthentication|port'

# Suivre les échecs d’auth
sudo tail -f /var/log/auth.log

# Vérifier ouverture du port depuis le client
nc -vz 89.80.61.108 2222

-----------------------------------------------------------------------------

### client
# Sur le client
cat ~/.ssh/id_ed25519.pub            # copier la ligne entière

# Sur le serveur
sudo -u teas mkdir -p /home/teas/.ssh
sudo -u teas nano /home/teas/.ssh/authorized_keys   # coller la ligne
sudo chown -R teas:teas /home/teas/.ssh
sudo chmod 700 /home/teas/.ssh
sudo chmod 600 /home/teas/.ssh/authorized_keys

# Sur chaque appareil
ssh-keygen -t ed25519 -C "portable"          # puis
ssh-copy-id -p 2222 -i ~/.ssh/id_ed25519.pub teas@89.80.61.108

# lance (souvent auto‑démarré sous KDE/GNOME)
eval "$(ssh-agent -s)"

# charge la clé une seule fois
ssh-add ~/.ssh/id_ed25519     # tape ta passphrase UNE fois

# vérifie
ssh-add -l                   # la clé doit apparaître


