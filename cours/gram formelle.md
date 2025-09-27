# Linguistique computationnelle — Organisation & Introduction

**Master 1 – Langue et Informatique – Semestre 1**
*Sophie Robert-Hayek*

---

## Organisation pratique

### Format des séances

* **2h30 de cours chaque mercredi**, découpés (approx.) en :

  1. **Correction du TP précédent** + **interrogation orale** (\~30 min)
  2. **Cours magistral (CM)** (\~1h30)
  3. **Implémentation en TP** des notions vues en CM (\~30 min)

> **Ressources du cours**
>
> * **Moodle** *(Clé d’inscription : `M1_2025`)*
> * **GitHub** *(ici)*

### Évaluation

* **Deux contrôles continus** annoncés selon l’avancement : **25% + 25%**
* **Partiel terminal** : **50%**

### Organisation des TP

* **Toujours signaler** si vous ne comprenez pas ou si **le rythme est trop rapide**.
* Chaque TP comprend :

  * un **socle commun** ;
  * des **questions “pour aller plus loin”** à terminer d’une semaine à l’autre et **corrigées ensemble**.

---

# Linguistique computationnelle : définitions et cas applicatifs

## Définition

> **Linguistique computationnelle** (aussi **Traitement Automatique du Langage naturel — TAL / NLP**) :
> utilisation d’**outils informatiques** pour **analyser**, **comprendre** et **générer** du **langage naturel**.

* Technologie **centrale** de l’ère de l’information, présente dans **tous les aspects** de la vie moderne.
* Discipline **nécessairement interdisciplinaire** :

  * **Linguistes** : structure du langage ;
  * **Mathématiciens** : modèles de langue, nouveaux paradigmes de calcul ;
  * **Informaticiens** : implémentation des outils.

## Domaines applicatifs (exemples)

* **Analyse de textes** : classification, **analyse de sentiments**, **analyse stylistique** ;
* **Génération de langage** : **chatbots**, **traduction automatique** ;
* **Traitement de la parole** : **reconnaissance** et **synthèse vocale**.

## Questions typiques du NLP

* **Un texte exprime-t-il une émotion ?**
* **Qui est l’auteur** d’un texte controversé ?
* **Peut-on traduire fidèlement** d’une langue à l’autre ?

---

## Exemples issus de la recherche de l’enseignante

* **Aligner deux textes et leurs traductions** à l’aide de **plongements sémantiques** (*semantic embeddings*).
* **Trouver les variantes intéressantes** en comparant deux textes.

  * *Ex.*

    * Phrase 1 : *le chat mange car il est beau*
    * Phrase 2 : *le chien mange parce que il est beau*
* **Sujets de mémoire** proches de ces thématiques : *en parler avec l’enseignante si intéressé·e*

---

# Objectifs du cours

* **Analyse automatique du langage** :

  * analyser les **mots** utilisés ;
  * analyser les **structures de phrases**.
* **Génération de textes** capables d’**imiter** le langage humain.
* **Annotation** des structures linguistiques du **mot** (nœud terminal) jusqu’à la **phrase** (arbre syntaxique).

---

# Niveaux d’analyse linguistique

## Définitions de base

* **Mot** : unité minimale **autonome** de sens ou de fonction dans une langue,
  sous forme **mot-forme** (*mangeons*) ou **lemmatisée** (*manger*).
* **Phrase** : unité **syntaxique autonome**, construite selon les règles d’une langue,
  qui **porte un sens complet** et **communique une information**.

> Pour étudier le langage naturel, on analyse :
>
> * les **unités lexicales** (*mots*) ;
> * les **règles syntaxiques** qui régissent leur **combinaison** en **structures hiérarchisées**.

## Ordre d’analyse adopté dans le cours

1. **Au niveau du mot** : catégories lexicales (Part-of-Speech), lemme, morphologie…
2. **Au niveau de la phrase** : organisation en **syntaxes/grammaires** (constituants, dépendances).

---

## Analyse au niveau du mot — Quels volets ?

* **Lemme** : forme de base (dictionnaires / analyse lexicale).
* **Catégorie** : **classe grammaticale** (*verbe, pronom, nom, …*).
* **Morphologie** : **informations grammaticales** portées par la flexion.
* **Sémantique** : **représentation du sens** d’un mot *(→ mentionnée ici, **pas l’objet** de ce cours)*.

> 🔎 **Ce cours se concentre sur** l’**analyse des catégories lexicales (POS / POS-tagging)**.

### Exemple de lemmatisation, POS et morphologie

**Phrase à analyser** : *Nous aimons réviser nos cours.*

| Mot-forme | Lemme   | Catégorie        | Traits morphologiques                          |
| --------- | ------- | ---------------- | ---------------------------------------------- |
| nous      | nous    | pronom personnel | 1ʳᵉ pers., pluriel, **sujet**                  |
| aimons    | aimer   | verbe            | 1ʳᵉ pers., pluriel, **présent**, **indicatif** |
| réviser   | réviser | verbe            | **infinitif**                                  |
| nos       | notre   | déterminant      | 1ʳᵉ pers., pluriel, **possessif**              |
| cours     | cours   | nom              | **masculin**, **pluriel**                      |

---

# Analyser la syntaxe d’une phrase

## Deux approches complémentaires

1. **Grammaire des constituants** :
   les mots sont regroupés en **constituants**/**phrases imbriquées** → **arbre syntaxique** (hiérarchique).
2. **Grammaire de dépendance** :
   relations **tête ↔ dépendants** entre mots ; chaque mot **dépend** d’un autre.

### Illustration (même phrase)

**Analyse en constituants** (schéma canonique) :

```
S
├─ NP
│  ├─ Det  Le
│  └─ N    chat
└─ VP
   ├─ V    mange
   └─ NP
      ├─ Det  la
      └─ N    souris
```

**Analyse en dépendance** (étiquettes typiques) :

```
Le   chat   mange   la   souris
det  nsubj   root   det   obj
```

> **But du cours (côté phrase)** :
>
> * **Annoter les mots** (nœuds terminaux) ;
> * **Construire**, à l’aide d’une **grammaire**, leur **arbre syntaxique**.

---

# Introduction aux grammaires formelles (aperçu)

* **Approche 1** : **par constituants** → arbres **hiérarchiques** (phrases, groupes nominaux/verbal, etc.).
* **Approche 2** : **par dépendances** → **graphe** orienté centré sur la **tête** et ses **relations**.

> **Chaînes de Markov** (mention) :
> modélisent la **probabilité** qu’un mot **appartienne à une catégorie** syntaxique (ou d’autres séquences) ; utiles comme **modèles séquentiels** probabilistes.

---

# Notes & rappels complémentaires (listes de fin)

* **Lire Jurafsky & Martin** (*Speech and Language Processing* ; livre en anglais, dispo en PDF).
* **Annotation des structures linguistiques** (mot & phrase) : **POS / POS-tagging**.
* **Évaluation** : 2 contrôles **25/25** + 1 contrôle **50** (cf. plus haut : **25% + 25% + 50%**).
* **Analyse automatique des mots** & **génération de textes** (objectifs du cours).
* **Outils** : **spaCy**, **Stanza**, **Flair**, **NLTK**.
* **Ingénierie logicielle** : cours **éventuel** en fin d’année.
* **Thème de recherche de la prof.** : **alignement de textes entre le latin et le grec** ; études sur la **diffusion** et la **transmission** des textes.

---

# Sémantique (mention hors périmètre principal du cours)

* **Analyse sémantique** : étude de **champs sémantiques** et **liens** entre mots ;
* **Word embeddings** : représentations vectorielles capturant des **proximités sémantiques**.
* *Ex.* : *le chat mange la souris* → similarités et relations sémantiques (non développées ici).

---
