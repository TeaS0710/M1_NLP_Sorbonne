 cd "/home/teas/programmes/KARCH" && { [ -d .git ] || (git init -b main || { git init && git branch -M main; }); } && git add -A && git commit -m "Import complet du dossier KARCH" || true && ssh-add ~/.ssh/id_ed25519_github_l3 >/dev/null 2>&1 || true && git remote remove origin 2>/dev/null || true && git remote add origin git@github-l3:TeaS0710/KARCH.git && git push -u origin main

