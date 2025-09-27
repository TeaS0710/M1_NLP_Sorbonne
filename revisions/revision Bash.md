---

# Fiche de révision Bash

---

## 1. Introduction

* Bash est le shell le plus courant sous Linux.
* Sert à : naviguer, manipuler fichiers, automatiser via scripts.

**Test rapide** : tape `echo "Bonjour $USER"` pour afficher ton nom d’utilisateur.

---

## 2. Commandes de base

```bash
pwd                  # Affiche /home/adrien (exemple)
ls -lh               # Liste fichiers avec tailles lisibles
cd /etc              # Aller dans /etc
mkdir projets        # Crée un dossier
touch notes.txt      # Crée un fichier vide
cp notes.txt notes.bak   # Copie fichier
mv notes.txt ancien.txt  # Renomme fichier
rm ancien.txt            # Supprime fichier
```

---

## 3. Navigation & chemins

```bash
cd ~/Documents        # Aller dans Documents (chemin relatif)
cd /var/log           # Aller dans log (chemin absolu)
ls .                  # Liste contenu du dossier courant
ls ..                 # Liste contenu du parent
```

Exemple :

```bash
cd ~/projets
cd ..
pwd   # revient dans /home/adrien
```

---

## 4. Gestion des droits

```bash
ls -l script.sh       # -rw-r--r-- 1 adrien adrien 120 sep 15 script.sh
chmod u+x script.sh   # Ajoute exécution à l’utilisateur
./script.sh           # Lancer le script
```

---

## 5. Redirections & pipes

```bash
echo "erreur fatale" > log.txt      # Écrase log.txt
echo "ajout" >> log.txt             # Ajoute à la fin
cat log.txt | grep "erreur"         # Cherche erreurs
ls /root 2> erreurs.txt             # Erreurs dans un fichier
ls /etc | sort | uniq | less        # Trier et lire page par page
```

---

## 6. Variables

```bash
nom="Adrien"
echo "Bonjour $nom"        # Bonjour Adrien
fichier="/etc/passwd"
echo "Fichier = $fichier"
```

Variables système :

```bash
echo $HOME     # /home/adrien
echo $PATH     # chemins des programmes
echo $$        # PID du shell
echo $?        # Code retour de la dernière commande
```

---

## 7. Fichiers & texte

```bash
grep "bash" /etc/passwd             # Cherche les utilisateurs bash
find /var/log -name "*.log"         # Trouve tous les fichiers .log
wc -l /etc/passwd                   # Nombre de lignes
sort noms.txt                       # Trie la liste
uniq noms.txt                       # Supprime doublons
cut -d: -f1 /etc/passwd             # Affiche uniquement les logins
awk -F: '{print $1,$3}' /etc/passwd # Affiche login + UID
sed 's/root/admin/g' fichier.txt    # Remplace root par admin
```

---

## 8. Processus & jobs

```bash
ps aux | grep firefox   # Cherche processus firefox
kill 12345              # Tue PID 12345
./long_script.sh &      # Lance en arrière-plan
jobs                    # Liste jobs
fg %1                   # Ramène job n°1
```

---

## 9. Historique & raccourcis

```bash
history | tail -5       # Affiche 5 dernières commandes
!!                      # Réexécute dernière commande
!42                     # Relance commande n°42 de l’historique
Ctrl + r                # Recherche interactive
```

---

## 10. Scripts Bash

### Exemple simple

```bash
#!/bin/bash
echo "Hello World"
```

Exécution :

```bash
chmod +x script.sh
./script.sh
```

### Variables & arguments

```bash
#!/bin/bash
echo "Nom du script : $0"
echo "Premier argument : $1"
echo "Nombre d’arguments : $#"
echo "Tous les arguments : $@"
```

Exemple : `./script.sh Adrien Paris`
→ affiche "Adrien" et "Paris".

### Conditions

```bash
#!/bin/bash
if [ $1 -gt 10 ]; then
  echo "Supérieur à 10"
elif [ $1 -eq 10 ]; then
  echo "Égal à 10"
else
  echo "Inférieur à 10"
fi
```

### Boucles

```bash
for i in {1..3}; do
  echo "Tour $i"
done
```

```bash
n=1
while [ $n -le 3 ]; do
  echo "Boucle n=$n"
  ((n++))
done
```

### Fonctions

```bash
dire_bonjour() {
  echo "Bonjour $1"
}
dire_bonjour Adrien
```

---

## 11. Substitution de commandes

```bash
date=$(date +%Y-%m-%d)
echo "Nous sommes le $date"
```

```bash
fichiers=$(ls *.txt)
echo "Liste des .txt : $fichiers"
```

---

## 12. Astuces pratiques

```bash
alias ll='ls -lh --color=auto'   # Raccourci
which python3                    # Localisation exécutable
man ls                           # Manuel complet
set -x                           # Mode debug
```

---

## 13. Exemple de script pratique : sauvegarde

```bash
#!/bin/bash
src=~/Documents
dest=~/sauvegardes/backup_$(date +%Y%m%d).tar.gz

tar -czf $dest $src
echo "Sauvegarde terminée : $dest"
```

---
