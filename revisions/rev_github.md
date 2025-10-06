```bash
bash << 'EOF'
set -euo pipefail

# ===== Variables à ajuster si besoin =====
DIR="/home/teas/programmes/prog S6"
REMOTE="git@github-l3:TeaS0710/L3_full_version.git"
NAME="TeaS0710"
EMAIL="vergneadrien65@gmail.com"
# =========================================

# 0) Nettoyage si tu as initialisé par erreur dans ton HOME
[ -d "$HOME/.git" ] && rm -rf "$HOME/.git"

# 1) Config globale Git
git config --global user.name  "$NAME"
git config --global user.email "$EMAIL"
git config --global init.defaultBranch main

# 2) Vérif/connexion SSH à GitHub via l'alias 'github-l3'
set +e
SSH_OUT="$(ssh -T -o BatchMode=yes github-l3 2>&1)"
set -e
if ! printf "%s" "$SSH_OUT" | grep -qi "successfully authenticated"; then
  echo "[!] Auth SSH GitHub non confirmée via 'github-l3'."
  if [ -f "$HOME/.ssh/id_ed25519_github_l3.pub" ]; then
    echo "Ajoute cette clé dans GitHub → Settings → SSH keys, puis relance :" 
    echo "-----8<-----"
    cat "$HOME/.ssh/id_ed25519_github_l3.pub"
    echo "-----8<-----"
  else
    echo "Vérifie ~/.ssh/config et ta clé dédiée (id_ed25519_github_l3)."
  fi
  exit 1
fi

# 3) Aller dans le bon dossier
cd "$DIR" || { echo "[!] Dossier introuvable: $DIR"; exit 1; }
echo "[i] Dossier: $(pwd)"

# 4) Init repo si besoin
if [ ! -d .git ]; then
  git init -b main || { git init; git branch -M main; }
fi

# 5) .gitignore (créé si absent)
if [ ! -f .gitignore ]; then
  cat > .gitignore <<'GI'
__pycache__/
*.pyc
.ipynb_checkpoints/
.venv/
venv/
.env
.vscode/
.idea/
.DS_Store
dist/
build/
*.egg-info/
*.zip
*.7z
*.tar
*.tar.gz
*.tgz
*.iso
*.mp4
*.mkv
*.pt
*.bin
GI
  echo "[i] .gitignore créé."
fi

# 6) Ajout + commit (si nécessaire)
git add -A
if ! git diff --cached --quiet; then
  git commit -m "Import complet cours & programmes L3 (archive)" || true
else
  echo "[i] Rien à committer."
fi

# 7) Remote + push
if git remote | grep -qx origin; then
  git remote set-url origin "$REMOTE"
else
  git remote add origin "$REMOTE"
fi

set +e
git push -u origin main
RC=$?
if [ $RC -ne 0 ]; then
  echo "[!] Push direct échoué. Tentative fetch + rebase..."
  git fetch origin && git pull --rebase origin main && git push -u origin main
  RC=$?
fi

if [ $RC -ne 0 ]; then
  echo "[!] Échec du push. Pour forcer (écrasement du remote) :"
  echo "    cd \"$DIR\" && git push -u origin main --force"
  exit $RC
fi

echo "✅ Push terminé."
EOF
```
