```bash

1) Inserer le chemin vers ton dossier qui contient ton programme python
cd /chemin/vers/ton/projet

2) Créer et activer l’environnement virtuel
# Si besoin, installe l’outil venv
sudo apt update && sudo apt install -y python3-venv

# Crée un venv local au projet (recommandé)
python3 -m venv .venv

# Active-le
source .venv/bin/activate

Pour quitter plus tard :
deactivate

3) Mettre pip à jour & installer les dépendances

python -m pip install --upgrade pip
pip install -r requirements.txt

```
