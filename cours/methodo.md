# M1SOL023 — Méthodologie de la Recherche

**Langue et Informatique — 2025–2026**
**Projet : Classification et Modèles Multimodaux**
**Responsables :** Laurence Devillers & Nour El Houda Ben Chaabene (Sorbonne Université)

---

## Résumé du projet

L’objectif est de conduire une expérience complète de classification automatique à partir d’un jeu de données choisi (texte et/ou audio). Le travail couvre l’ensemble de la chaîne : préparation des données → représentations → apprentissage → évaluation, en explorant à la fois des méthodes classiques et des modèles récents (LLM, multimodal).

* **Livrables :** rapport + code
* **Poids :** moitié de la note de contrôle continu
* **Oral :** session de janvier 2026

```
Projet de classification (texte / audio / multimodal)
├─ Données (collecte, préparation)
├─ Représentations (Texte / Audio / Fusion)
├─ Modèles (classifieurs)
├─ Évaluation (métriques, matrices)
└─ Analyse critique (erreurs, limites, extensions)
```

---

## Objectifs

* Mettre en place une chaîne complète de classification : préparation, représentation, apprentissage, évaluation.
* Expérimenter des méthodes classiques (scikit-learn) et modernes :

  * **Texte :** TF‑IDF, Flaubert/BERT
  * **Audio :** Wav2Vec
  * **Multimodal :** combinaison texte+audio (ex. Whisper pour transcription)
* Comparer les performances selon représentations et algorithmes.
* Analyser de façon critique les résultats et proposer des améliorations.

### Objectifs ↔ livrables

| Objectif              | Preuve dans le rapport           | Trace dans le dépôt              |
| --------------------- | -------------------------------- | -------------------------------- |
| Chaîne complète       | Section « Méthode » + pipeline   | `preprocess/`, `train/`, `eval/` |
| Méthodes variées      | Tableau de résultats comparatif  | Notebooks/expériences distincts  |
| Comparaison des perfs | Matrices + métriques macro/micro | `results/` (CSV/JSON)            |
| Analyse critique      | Section « Discussion »           | `error_analysis/`                |

> Astuce : garder une correspondance 1‑à‑1 entre sections du rapport et répertoires du dépôt.

---

## Méthodologie (étapes)

1. **Préparation / nettoyage** du jeu de données (instances `X`, classes `y`).
2. **Représentations** :

   * Texte : sac de mots, TF‑IDF, embeddings LLM
   * Audio : Wav2Vec / features dérivées
3. **Classifieurs** : Naïve Bayes, SVM, arbres, forêts, réseaux simples.
4. **Fusion multimodale** (texte+audio : précoce, tardive, hybride).
5. **Évaluation** : accuracy, précision, rappel, F1, AUC/ROC, AUPRC, matrices de confusion.
6. **Discussion** : erreurs typiques, limites, ouverture (autres corpus/langues/modalités).

```
Données brutes
  └─► Préparation (nettoyage, normalisation, split stratifié)
        ├─► Texte : BOW / TF‑IDF / Embeddings
        ├─► Audio : Wav2Vec / features
        └─► Fusion : précoce | tardive | hybride
              └─► Classifieurs (NB, SVM, Arbres, RF, RN)
                    └─► Évaluation (Accuracy, Précision, Rappel, F1, AUC/PR)
                          └─► Analyse d’erreurs & Perspectives
```

### DataSet

```
# Dataset Card — [Nom]
Source & licence :
Taille & classes :
Préparation (nettoyage/équilibrage) :
Splits (train/val/test, seeds, stratification) :
Biais & limites :
Notes éthiques (si applicable) :
```

### Journal d’expériences

```
# Exp Log — [Run ID]
Date/heure :
Seed :
Données (version, split) :
Représentation :
Modèle & hyperparamètres :
Résultats (accuracy, macro‑F1, micro‑F1) :
Matrice de confusion : [chemin/figure]
Erreurs typiques :
Remarques / suites :
```

---

## Plan rapport Type

1. **Introduction** — tâche, jeu de données, objectifs.
2. **État de l’art** — classification, LLM, multimodal.
3. **Corpus** — taille, classes, constitution, statistiques, exemples.
4. **Méthode** — représentations, algorithmes, paramètres, choix justifiés.
5. **Résultats** — tableaux/figures, comparaisons, analyse d’erreurs.
6. **Conclusion & perspectives** — synthèse, limites, pistes futures.
7. **Annexes** — organisation du code, consignes techniques, exemples.

> Emplacements de figures

```
Figure 1 — Pipeline de traitement
Figure 2 — Matrice de confusion (modèle X)
Figure 3 — Courbe PR (classe positive) / Courbe ROC (macro)
Figure 4 — Barplot des erreurs par classe (top‑5 confusions)
Table 1 — Comparaison des modèles (moyenne ± écart‑type, k‑fold)
```

---

## Rendu attendu

* **Rapport** : PDF (\~10 pages hors annexes)
* **Code** : Python `.ipynb` et/ou `.py`, documenté
* **Dépôt final** : 04/01/2026 sur Moodle (code + rapport)

### Checklist

* [ ] Rapport PDF ≤ 10 pages (hors annexes)
* [ ] Code clair + README + `requirements.txt`
* [ ] Résultats reproductibles (seeds, splits)
* [ ] Dossier `results/` + journaux d’expériences

---

## Memo

**Matrice binaire**

|              | Prédit : Positif | Prédit : Négatif |
| ------------ | ---------------: | ---------------: |
| **Réel : +** |               VP |               FN |
| **Réel : −** |               FP |               VN |

```
Précision = VP / (VP + FP)
Rappel    = VP / (VP + FN)
F1        = 2 * (Précision * Rappel) / (Précision + Rappel)
Accuracy  = (VP + VN) / (VP + FP + FN + VN)
```

**Matrice multi‑classes (3 classes)**

| Réel \ Prédit |  C1 |  C2 |  C3 |
| ------------- | --: | --: | --: |
| **C1**        | n11 | n12 | n13 |
| **C2**        | n21 | n22 | n23 |
| **C3**        | n31 | n32 | n33 |

**Quand utiliser quelle métrique ?**

| Contexte            | Métrique prioritaire | Pourquoi                   |
| ------------------- | -------------------- | -------------------------- |
| Classes équilibrées | Accuracy             | Vue globale                |
| Coût FP élevé       | Précision            | Éviter FP                  |
| Coût FN élevé       | Rappel               | Ne pas rater les vrais cas |
| Fort déséquilibre   | Macro‑F1 / AUPRC     | Sensible aux minoritaires  |

**Courbes (schémas textuels)**

```
Courbe PR
Précision
1.0 |■■■■■■■■■■
    |■■■■■■■
0.5 |■■■
    +-------------- Rappel

Courbe ROC
TPR
1.0 |        ■■■■
    |     ■■■
0.5 |  ■■
    +-------------- FPR
```

---

## TODO

* Faire le projet (binômes, mardi après‑midi) — **très important**
* Faire le TD 1 de Nour (mardi après‑midi) — **à faire**
* Rendre les programmes à Nour (début mardi après‑midi) — **urgent**

**Kanban (à copier dans le README)**

```
À faire
- Choisir corpus + licence
- Définir splits & seeds
- Implémenter pipelines texte/audio

En cours
- Entraînement SVM (TF‑IDF)
- Wav2Vec feature extraction

Fait
- Nettoyage corpus v1
- Baseline Naïve Bayes
```

---

# CM2 — Méthodologie : Classification & IA

## 1) Classification automatique

### 1.1 Jeu de données & découpage

* **Jeu de données** : ensemble des exemples disponibles.
* **Découpage classique** :

  * **Entraînement** : \~80 % (apprentissage des paramètres)
  * **Test** : \~20 % (évaluation sur données jamais vues)
* **Bonne pratique** : validation croisée (k‑fold) pour réduire la variance.

```
Corpus complet
  ├─► Train (CV k‑fold stratifiée)
  └─► Test (hold‑out, jamais vu)
Note : pas de fit sur Test ; réglages via CV uniquement.
```

### 1.2 Classifieur (ex. arbre de décision)

* Modèle qui segmente l’espace des données via des questions successives sur les attributs (seuils/tests) jusqu’aux feuilles.
* **Avantages** : interprétable, rapide.
* **Limites** : sur‑apprentissage sans élagage.

```
Noeud 0 : [cond A]
├─ Vrai → Noeud 1 : [cond B]
│         ├─ Vrai → Feuille : Classe X
│         └─ Faux → Feuille : Classe Y
└─ Faux → Noeud 2 : [cond C]
          ├─ Vrai → Feuille : Classe Z
          └─ Faux → Feuille : Classe W
```

### 1.3 Rappel, précision, F‑mesure

Voir définitions et formules ci‑dessus (section « Évaluation & métriques »).
En données déséquilibrées, l’accuracy est trompeuse : privilégier Précision/Rappel/F1, AUPRC, AUC‑ROC.

### 1.4 Décider si le modèle a « bien appris »

* Examiner macro‑F1, courbes ROC/PR, matrice de confusion.
* Contrôler l’overfitting : écart train/test, validation croisée, régularisation, élagage (arbres), early stopping (réseaux).

| Indice                     | Observation            | Remède rapide                         |
| -------------------------- | ---------------------- | ------------------------------------- |
| Score train > val/test     | Écart important        | Régulariser, plus de données, élaguer |
| Variance forte entre folds | Scores instables       | CV stratifiée, ajuster HP             |
| Erreurs sur minoritaires   | Confusions récurrentes | Pondération, re‑sampling              |

---

## 2) Familles de classification

### 2.1 Supervisée vs non supervisée

```
IA (Apprentissage)
├─ Supervisé : données étiquetées (X, y)
│  ├─ Classification (étiquettes discrètes)
│  └─ Régression (valeurs continues)
└─ Non supervisé : données non étiquetées (X)
   ├─ Clustering (ex. k‑means)
   └─ Réduction de dimension (PCA, t‑SNE, UMAP)
```

| Cadre     | Tâche          | Exemple             |
| --------- | -------------- | ------------------- |
| Supervisé | Classification | Détection de spam   |
| Supervisé | Régression     | Prédire une durée   |
| Non sup.  | Clustering     | Regrouper par thème |
| Non sup.  | Réduction dim. | Visualiser en 2D    |

### 2.2 Auto‑supervisé & renforcement

```
Apprentissages « spéciaux »
├─ Auto‑supervisé : cibles créées à partir des données
└─ Renforcement (RL) : apprentissage par récompense
```

* Auto‑supervisé : pré‑entraînement (masquage/prédiction, contrastif…).
* RL : agent, environnement, récompenses, politique.

---

## 3) Chaîne « parole → parole » (exemple)

Thèmes : parole (parlée, écrite, signée), compréhension, éthique, historique des approches.

```
Signal audio ─► STT ─► Compréhension/raisonnement ─► NLG ─► TTS ─► Audio
```

---

## 4) Anthropomorphisme, vision technologique & éthique

* **Anthropomorphisme** : attribuer des intentions/émotions à des machines.
* **Vision holistique** : aspects techniques, sociaux, juridiques, éthiques (biais, transparence, responsabilité, impact).
* **Prudence terminologique** : préférer des définitions opérationnelles (capacités mesurables) au terme générique « intelligence ».

**Mémo éthique (court)**

```
Sujet :
Parties prenantes :
Biais/risques :
Mesures de mitigation :
Références (≥ 5) :
```

---

## 5) Deux traditions en IA : symbolique vs connexionniste

```
Approches IA
├─ Symbolique (GOFAI)
│  ├─ Connaissances explicites (règles, logiques)
│  ├─ Raisonnement déductif / inférentiel
│  └─ Forte explicabilité, mais rigidité
└─ Connexionniste (réseaux de neurones)
   ├─ Apprentissage par données et gradients
   ├─ Représentations distribuées/probabilistes
   └─ Grande performance, explicabilité plus difficile
```

| Aspect        | Symbolique    | Connexionniste    |
| ------------- | ------------- | ----------------- |
| Connaissance  | Règles        | Poids appris      |
| Données       | Peu           | Massives          |
| Explicabilité | Haute         | Faible (XAI)      |
| Robustesse    | Fragile bruit | Souvent meilleure |

> Pratique actuelle : approches **hybrides** (neurosymboliques).

---

## 6) Calcul & matériel

* **GPU/TPU** : calcul parallèle massif pour tenseurs et rétropropagation.
* **CPU** : pré/post‑traitements, orchestration.

```
Applis ML
  └─ Frameworks (PyTorch / TF)
       └─ CUDA/ROCm / BLAS
            └─ GPU/TPU (parallélisme)
                 └─ CPU (orchestration)
```

---

## 7) Définitions essentielles

* **Intelligence artificielle (IA)** : théories/algorithmes/logiciels visant des capacités cognitives spécifiques, mesurées par des tâches.
* **Apprentissage supervisé** : à partir de données étiquetées.
* **Apprentissage non supervisé** : découverte de structures sans étiquettes.
* **Apprentissage auto‑supervisé** : tâches prétextes issues des données (masquage, contraste).
* **Apprentissage par renforcement (RL)** : optimisation d’une politique via récompense.
* **Deep Learning** : réseaux profonds ; optimisation par gradient.
* **Réseau de neurones** : neurones artificiels (linéaire + non‑linéaire) organisés en graphe.

**Fiche concept**

```
Concept : [Nom]
Définition opératoire :
Hypothèses / limites :
Exemples / contre‑exemples :
Mesure / évaluation :
```

---

## 8) Mini‑recap

### 8.1 Arbre de decisions

```
Si (x.feature_1 ≤ 2.7) ?
├─ Oui  → Feuille : Classe A
└─ Non → Si (x.feature_2 > 5.1) ?
         ├─ Oui  → Feuille : Classe B
         └─ Non  → Feuille : Classe C
```

### 8.2 Pipeline type

```
Données brutes
  ↓ (nettoyage / normalisation / équilibrage)
Jeu d’entraînement / validation croisée
  ↓ (vectorisation / features)
Entraînement du classifieur (ex. arbre)
  ↓ (réglage d’hyperparamètres)
Évaluation (matrice de confusion, F1, ROC/PR)
  ↓
Test final (généralisation) → Déploiement
```

**Tableau de résultats type**

| Modèle | Représentation | Accuracy | Macro‑F1 | Micro‑F1 |
| ------ | -------------- | -------: | -------: | -------: |
| NB     | TF‑IDF         |          |          |          |
| SVM    | TF‑IDF         |          |          |          |
| RF     | Embeddings     |          |          |          |
| BERT   | CLS pooling    |          |          |          |

---

## 9) Corrections de formulations (ref)

* classification **supervisée / non supervisée**
* **compréhensions** profondes (pas « compréhensions *de* … »)
* **speech‑to‑speech** (parole‑à‑parole)
* **anthropomorphisme**
* « **intelligence** » : terme galvaudé, contextualiser
* **connexionniste**
* **non prédéterminé**
* **processeurs multiples / GPU**
* **capacités cognitives** de l’humain
* **apprentissage** (orthographe, accords)

---

## 10) erreurs fréquentes

* Séparer strictement entraînement et test (pas de fuite de données).
* En données déséquilibrées : privilégier F1, AUPRC à l’accuracy.
* Pour arbres : contrôler profondeur, min‑samples‑leaf, élaguer.
* Utiliser la **stratification** dans les splits et la CV.
* Reporter moyenne ± écart‑type (CV) ou intervalles de confiance.

**Check list « bonnes pratiques»**

* [ ] Split **stratifié** + **seed** fixé
* [ ] **CV k‑fold** pour les hyperparamètres
* [ ] **Aucune** fuite (fit uniquement sur train)
* [ ] Comparaisons **iso‑splits** entre modèles
* [ ] **Macro‑F1** reportée si déséquilibre
* [ ] Journal d’expériences à jour

---

## 11) resumé

* La classification mesure la **généralisation** d’un modèle.
* Les métriques clés (Précision, Rappel, F1) dérivent de la **matrice de confusion**.
* **Supervisé** (labels) vs **non supervisé** (structure) vs **auto‑supervisé** vs **renforcement**.
* **Symbolique** (règles, explicable) ↔ **connexionniste** (données, performance) → **hybrides**.
* Le **matériel** (GPU/TPU) est central pour l’IA moderne à grande échelle.
