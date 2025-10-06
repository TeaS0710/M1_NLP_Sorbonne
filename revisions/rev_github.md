```bash
cd /chemin/vers/ton/dossier

git init -b main 2>/dev/null || { git init && git branch -M main; }

# (optionnel) .gitignore minimal
cat > .gitignore << 'EOF'
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
EOF

git add -A
git commit -m "Import complet cours & programmes L3 (archive)"

# Utilise l’alias qui force la bonne clé
git remote remove origin 2>/dev/null || true
git remote add origin git@github-l3:TeaS0710/L3_full_version.git

# Si le repo GitHub est vide :
git push -u origin main

# Si le repo n’est PAS vide :
# git fetch origin
# git pull --rebase origin main
# git push -u origin main
```
