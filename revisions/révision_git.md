# Guide Git & GitHub — clair, rapide et sans pièges

> Objectif : t’aider à **bosser propre** (local ↔ GitHub), éviter les pièges habituels et savoir **rattraper** une situation.
> Public : usage solo ou petite équipe. Linux/Ubuntu, terminal.

---

## 0) Les 3 idées à retenir

1) **Local** → *stage* → **commit** → **push** *(vers GitHub)*
2) **Pull --rebase** avant de pousser, surtout si tu n’étais pas seul.
3) **Branche par feature** (`feat/…`, `fix/…`), PR pour fusionner proprement.

---

## 1) Installer & configurer (une fois)

```bash
sudo apt install -y git

# Ton identité
git config --global user.name  "Adrien"
git config --global user.email "adrien@example.com"

# Branche par défaut = main
git config --global init.defaultBranch main

# (Option) Améliorations confort
git config --global pull.rebase true
git config --global rebase.autoStash true
git config --global core.editor "nano"   # ou "code --wait", "vim", etc.
```

---

## 2) Accès GitHub par SSH (recommandé)

```bash
ssh-keygen -t ed25519 -C "adrien@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
```

- Colle la clé publique dans **GitHub → Settings → SSH and GPG keys → New SSH key**.
- (Facultatif) `~/.ssh/config` :

```sshconfig
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519
  IdentitiesOnly yes
```

- Test :
```bash
ssh -T git@github.com
```

---

## 3) Démarrer un projet **local → GitHub**

Dans le dossier de ton projet (ex. `projet_class_pol`) :

### 3.1 `.gitignore` adapté Python / ton dépôt
Crée `./.gitignore` :

```gitignore
# Environnements & caches
.venv/
__pycache__/
*.pyc

# Données & sorties lourdes (ex: ton pipeline)
data/raw/
data/interim/
data/processed/
models/
reports/
logs/
tmp/
*.spacy
*.bin
*.pth

# Éditeurs / OS
*.kate-swp
*.swp
*~
.DS_Store
```

> Astuce : si tu veux garder l’arborescence vide dans Git, mets des `README.md` dans ces dossiers.

### 3.2 Premier commit & push
```bash
git init
git add -A
git commit -m "chore: initial commit (squelette projet)"

# Crée le repo vide sur GitHub (via l'UI), puis :
git remote add origin git@github.com:<USER>/<REPO>.git
git branch -M main
git push -u origin main
```

---

## 4) Workflow **quotidien**

```bash
# Voir où tu en es
git status

# Visualiser les changements
git diff                      # non indexés
git add <fichier>             # stage ciblé
git add -A                    # stage tout

# Commit local
git commit -m "docs: maj README (sync Makefile)"

# Récupérer avant de pousser (propre)
git pull --rebase

# Envoyer sur GitHub
git push
```

> Raccourci quand les fichiers sont **déjà suivis** (tracked) : `git commit -am "msg"` (équivaut à `git add` sur fichiers **modifiés** seulement).

---

## 5) Branches & PR (propre en équipe)

### 5.1 Créer / basculer
```bash
git checkout -b feat/tei-split          # crée + switch
# ... code ...
git commit -m "feat: split TEI en train/job"
git push -u origin feat/tei-split
```

Ouvre une **Pull Request** sur GitHub. Après merge :
```bash
git checkout main
git pull --rebase
git branch -d feat/tei-split
git push origin --delete feat/tei-split   # optionnel : supprime côté GitHub
```

### 5.2 Rebase vs Merge (résumé utile)
- **Merge** : garde l’historique “tel quel”, crée un commit de fusion.
- **Rebase** : réécrit tes commits “au-dessus” de `main` → historique **linéaire** plus lisible.
Recommandation : `git pull --rebase` pour sync, PR en “rebase & merge” ou “squash & merge”.

---

## 6) Rattraper et annuler (sécurité)

### 6.1 Avant commit
```bash
git restore <fichier>          # annule changements dans le fichier
git restore --staged <fichier> # retire du stage
```

### 6.2 Après commit (non poussé)
```bash
git commit --amend             # corrige le dernier commit (message/contenu)
git reset --soft  HEAD~1       # annule le commit, garde les changements staged
git reset --mixed HEAD~1       # annule le commit, changements non staged
git reset --hard  HEAD~1       # annule commit + changements (DANGEREUX)
```

### 6.3 Après push
- **Revert public et propre** :
```bash
git revert <sha_du_commit>
git push
```

### 6.4 Perdu quelque chose ?
```bash
git reflog                     # l’historique caché des HEAD
# récupère un état :
git checkout -b rescue <sha>
```

---

## 7) Stash (mettre de côté vite fait)

```bash
git stash push -m "wip tei parser"
# ... change de branche ...
git stash list
git stash pop                  # réapplique et supprime la stash
```

---

## 8) Tags & releases

```bash
git tag v0.1.0
git push origin v0.1.0
```

Sur GitHub, crée une **Release** depuis le tag (notes de version, binaries, etc.).

---

## 9) Fichiers lourds & données

- Évite de pousser `.venv`, `data/`, `models/`, `logs/` (utilise `.gitignore`).
- Si tu dois versionner de **gros artefacts** : regarde **Git LFS** (mais coûteux côté quotas).

---

## 10) Dépannage express

- **`Permission denied (publickey)`**
  - Ajoute la clé à l’agent : `ssh-add -l` ; remote en SSH ? `git remote -v`
- **`non-fast-forward`** lors du push
  - Tu n’as pas la dernière version : `git pull --rebase` puis `git push`
- **Conflits de merge**
  - Ouvre les fichiers, cherche `<<<<<<<`… Résous, puis :
    ```bash
    git add <fichier_resolu>
    git rebase --continue   # ou git merge --continue
    ```
- **Tu as push des trucs à ignorer (ex. .venv)**
  ```bash
  echo ".venv/" >> .gitignore
  git rm -r --cached .venv
  git commit -m "chore: nettoie index (.venv ignoré)"
  git push
  ```

---

## 11) Convention de messages de commit (lisibles)

Format recommandé (Conventional Commits) :
```
type(scope): message bref à l’infinitif
```
Exemples :
- `feat(tei): ajout split stratifié`
- `fix(train): corrige seed fixe + fuite job`
- `docs: synchronise README avec Makefile`

---

## 12) Mini “cheat sheet” (à garder sous la main)

```bash
# État / différences / historique
git status
git diff
git log --oneline --graph --decorate -n 20

# Stage / Unstage
git add -A
git restore --staged <f>

# Commit / Amend
git commit -m "msg"
git commit --amend

# Sync / Push
git pull --rebase
git push

# Branches
git checkout -b feat/xyz
git branch -d feat/xyz
git push origin --delete feat/xyz

# Undo / Rescue
git reset --soft HEAD~1
git revert <sha>
git reflog
```

---

### Bonus — Astuces pour ton dépôt actuel

- Ajoute au `.gitignore` : `*.kate-swp`, `logs/`, `tmp/`, `reports/`, `models/`, `data/*` (sauf `data/README.md` pour garder la structure).
- Utilise `git pull --rebase` par défaut (déjà config ci-dessus).
- Pense aux **branches courte durée** : `feat/…`, `fix/…`, `docs/…` ; fais une PR même solo pour garder un historique clean.

---
