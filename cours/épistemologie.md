# Épistémologie — Cours 1

**MASTER M1 (2025–2026) — « Information et Communication »**
**Prof. L. Devillers** — [devil@lisn.fr](mailto:devil@lisn.fr)

---

## Plan du cours

*(12 cours de 1h, 12 TD de 1h30)*

**Partie 1 : Informatique et histoire**

* Épistémologie : définition, principes
* Informatique : codage, modèle, évaluation

**Partie 2 : Épistémologie des sciences humaines et de l’informatique**

* En linguistique
* En sociologie
* En vie artificielle et robotique

**Partie 3 : Éthique du chercheur**

---

## En pratique — Évaluation

* **Contrôle continu** : tests sur table
* **Examen** (modalités précisées ultérieurement)

---

## Étude de l’informatique en tant que science

* **Cours 1** : Informatique et histoire
* **TD1** : Machine de Turing

---

# Épistémologie

* L’**épistémologie** est un terme apparu au début du XXᵉ siècle, dans un moment de **crise des savoirs**, pour définir la **science de la réflexion sur la science**.
* **Kant** est souvent considéré comme un **père fondateur** de l’épistémologie.
* L’épistémologie désigne **l’étude des sciences**. Son rôle est à la fois **d’analyser, d’étudier et de critiquer** toutes les disciplines scientifiques (mathématiques, chimie, biologie, physique, médecine, etc.), notamment à travers la **critique de leurs méthodes** et de leurs **découvertes**.

---

## Épistémologie de l’informatique

L’épistémologie de l’informatique est la branche de l’épistémologie qui prend pour objet d’étude **l’informatique en tant que science**, afin d’en déterminer :

* **Objets** : ce(ux) qui la constitue(nt) ;
* **Principes, concepts fondamentaux, théories, résultats** ;
* **Modes de construction de connaissances** : processus d’**inférence**, **émergence** de nouveaux concepts, **moteurs d’évolution** ;
* **Fondements, origine, portée objective** : ce qui la **justifie** dans le concert des sciences.

---

# Histoire de l’informatique (repères)

* **Logique** — IVᵉ siècle av. J.-C., Grèce
* **Algorithme** — 850 ap. J.-C., Bagdad (Irak)
* **Machines programmables** — XIXᵉ siècle (contexte luddiste, 1812, UK)
* **Algèbre de Boole** — \~1830, UK, **George Boole**
* **Première machine mathématique universelle** — 1834, UK, **Charles Babbage**
* **Machine de Turing** — 1936–1939, UK, **Alan Turing**
* **Prémices de l’IA** — « La machine peut-elle penser ? »
* **Premier ordinateur** — Résulte de siècles de logique et de théorie du raisonnement ; **1947 : John von Neumann**

---

## Informatique — Définition

* **Néologisme (1962)** créé par **Philippe Dreyfus** (ESPCI, professeur d’informatique à Harvard, directeur de BULL, vice-président de Cap Gemini) à partir de **« information »** et **« automatique »**.
* **Académie française (1966)** :

  > « La science du traitement rationnel, notamment par des machines automatiques, de l’information considérée comme le support des connaissances humaines et des communications dans les domaines techniques, économiques et sociaux. »
* Les **modèles informatiques** sont des **approximations** de la réalité.

### Objets de l’informatique

Trois objets (du plus abstrait au plus concret) :

1. Le **concept d’information**
2. Le **concept d’algorithme**
3. Le **concept de machine**

> Définition opératoire : **science du traitement de l’information par une machine**.
> **IA** : pas une science autonome en elle-même, mais un **domaine scientifique** au croisement de plusieurs disciplines.

---

# Méthodes de calcul — Algorithme

**Objectifs :**

* Formaliser la notion de **calcul** : qu’est-ce qu’une « **méthode effective** de calcul » ?
* Qu’est-ce qu’un **algorithme** ? Les **automates finis** ou **automates à pile** suffisent-ils, alors que nos ordinateurs ont un **nombre fini d’états** ?
* **Peut-on tout calculer ?** Il existe des **limites** aux automates finis/à pile : y en a-t-il à nos ordinateurs ?
* **Que peut-on calculer efficacement ?** Qu’est-ce que cela signifie ?
* Pourquoi certains problèmes sont-ils **durs** et d’autres **faciles** ?

## Algorithmes (1)

* « **Processus de résolution d’un problème par le calcul** », « **méthode effective** de calcul » — notion intuitive.
* Traces anciennes : **Babyloniens** (actuel Irak), 2ᵉ millénaire av. J.-C. (commerce, impôts).
* Grecs : **algorithme d’Euclide** (IIIᵉ s. av. J.-C.) pour le **pgcd**.
* **Étymologie** : mathématicien perse **Al-Khwarizmi** (IXᵉ s. ap. J.-C.) — a aussi donné « **algèbre** » ; étude systématique des algorithmes.
* **Machines et automates** (XVIIᵉ–XVIIIᵉ) : **Pascaline** (1642), **Leibniz** (1673), etc.

## Algorithmes (2)

* Algorithmes **géométriques** (règle & compas).
* Fin XIXᵉ–début XXᵉ : **formalisation des mathématiques** (axiomes, systèmes de preuve). Peut-on **tout** résoudre par algorithme ?
* **Hilbert (1900)**, 10ᵉ problème : « Trouver un **algorithme** déterminant si une **équation diophantienne** a des solutions. » (coefficients entiers, solutions entières).
* **Hilbert (1928)**, **problème de la décision** (*Entscheidungsproblem*) : donner un **algorithme** capable de décider si un **énoncé mathématique** est vrai.

## Algorithmes (3)

* **Années 1930** : **Church** (λ-calcul), **Turing** (machine de Turing), etc. proposent des **formalismes** de la notion d’algorithme ; ils montrent qu’un **algorithme général pour le problème de la décision n’existe pas**.
* **Matiyasevich (1970)** : pas d’algorithme pour décider si une **équation diophantienne** a une solution.

---

## Décidabilité

* Un **problème de décision** est une question mathématiquement définie sur des paramètres **manipulables informatiquement**, appelant une réponse **oui/non**.

  * Ex. : **Voyageur de commerce** — existe-t-il un chemin passant par toutes les villes, de longueur < d ?
* Un problème de décision peut être **indécidable** s’il **n’existe aucun programme** permettant de le résoudre (sans restriction de mémoire/temps), ce qu’on formalise par l’**impossibilité sur machine de Turing**.
* Certains problèmes **décidables** sont **non traitables en pratique** (complexité trop grande).
* La **théorie de la complexité** fournit une **hiérarchie** des complexités formelles.

---

# L’ordinateur : système artificiel intelligent (historique)

Deux grandes **rencontres** entre trois **histoires millénaires** :

* du **calcul**, du **raisonnement**, de la **mathématique** ;
* des **instruments** et **systèmes de calcul** ;
* des **machines** et **automates**.

**Rencontres majeures :**

* **1834** : **Charles Babbage** — première machine mathématique **universelle**
* **1947** : **John von Neumann** — premier **ordinateur** (aboutissement de la logique mathématique et de la théorie du raisonnement)

---

## La machine analytique de Babbage — l’ancêtre des ordinateurs

* **Le Moulin (Mill)** : effectue les **calculs** → équivalent du **processeur** (UAL).
* **Le Magasin** : **stocke** les chiffres → équivalent de la **mémoire**.
* **Sorties** : résultats **imprimés**.
* **Commandes** : **cartes perforées** (héritage des métiers à tisser) → équivalent des **programmes**.
* La machine complète aurait été un **enchevêtrement de roues/engrenages** mus par la **vapeur**, de la taille d’une **locomotive**.

---

## Le premier ordinateur de von Neumann (1903–1957)

**Architecture (modèle à programme enregistré)** :

1. **UAL / unité de traitement** : opérations de base
2. **Unité de contrôle** : séquençage des opérations
3. **Mémoire** : **données** + **programme**

   * **Mémoire vive** (en cours)
   * **Mémoire de masse** (base)
4. **Entrées/Sorties** : communication avec l’extérieur

---

## Premiers ordinateurs (repères)

* **1949–1951** : premier **temps réel** (MIT)
* **1950** : invention de l’**assembleur** (Maurice V. Wilkes, Cambridge)
* **1951** : premier ordinateur soviétique **MESM**
* **1951** : **Gamma 2** (Compagnie des Machines Bull)
* **1952** : **IBM 701** (défense US, 19 ex.)
* **1952** : **CUBA** (Calculateur Universel Binaire de l’Armement), premier ordinateur français (SEA)
* **1953** : **IBM 650** (1 000 ex., universités)

---

# Révolution informationnelle

## Années 1950 → 1970–1980

* **Années 1950** : usages **scientifiques** et **militaires**.
* Fin **1950s** : remplacement des **machines mécanographiques** (grandes entreprises, administrations d’État) pour la **gestion**.
* Extension à l’**industrie de process** (chimie, pétrochimie, cimenteries, centrales électriques) et aux **services** (banques, assurances).
* **Années 1970** : **microprocesseurs** puis **micro-ordinateurs** ; **téléinformatique** (réseaux, bases de données), logiciels **interactifs**.
* **Années 1980** : diffusion massive ; néologismes : **bureautique**, **robotique**, **productique**, **télématique** ; apparition croissante d’applications **grand public**.

## Logiciels de plus en plus complexes

* Jusqu’en **1985** : ordinateurs **institutionnels**.

  * **1950–1960** : logiciels développés **en interne** ; distribution limitée.
  * **Années 1970** : **multi-utilisateur**, **interfaces graphiques**, **concurrence**, **BD**, **temps réel** ; premiers **éditeurs** ; logiciels **biens marchands**.
  * **Depuis 1973**, et surtout **années 1980** (PC) : **grande distribution**, **progiciels** orientés **consommateur**.

* **1985–2000** : **systèmes distribués**, **Internet**, **client-serveur**, **cloud computing** ; POO et **conception orientée objet** ; logiciels intégrés dans des **écosystèmes collectifs**.

### Architecture client–serveur (1987)

* Application **scindée** en deux processus sur deux ordinateurs différents (**client**/**serveur**).
* Le client **formule des requêtes**, le serveur **traite** et **répond**.
* **Protocole** : format des requêtes/réponses.
* Adoption massive dans les **BD** (croissance forte années 1990).

### Cloud computing

* **Informatique en nuage** : **déport** de traitements sur des **serveurs distants** (vs locaux/poste client).
* Francisations : **informatique virtuelle/dématérialisée/infonuagique**.

---

# Programmation orientée objet (POO)

* Paradigme élaboré par **Alan Kay** (années 1970).
* Définition et interaction de **briques logicielles** appelées **objets**.
* Un objet représente un **concept/entité** (voiture, personne, page de livre), possède **structure** et **comportement**, et **communique** avec ses pairs.
* On **représente** objets et **relations** ; la **communication** réalise les fonctionnalités.

## Langages orientés objet (exemples)

* **Java (1995)**, **C# (2001)**, **Objective-C (1986)**, **Eiffel (1986)**, **Python (1990)**, **Ruby (1995)**, **C++ (1983)**, **Ada (1980)**, **PHP (1994)**, **Smalltalk (1969)**, **LOGO (1970)**, **AS3 (1998)**, …
* Deux grandes catégories : **à classes** et **à prototypes** ; styles **fonctionnel** (ex. CLOS/Lisp objet), **impératif** (C++, Java), ou **hybride** (Python, OCaml).
* **Indice TIOBE** : mesure mensuelle de **popularité** (depuis 2002), « **langage de l’année** » = plus forte croissance.

---

# Logiciels et IA (composants)

* **Reconnaissance de formes**
* **Déduction automatique**
* **Traduction automatique**
* **Exploration de données**

- montée des **logiciels libres** et **plateformes/outils** ouverts (ex. **Weka** pour la reconnaissance de formes).

---

# Impacts de la révolution informationnelle

* **Vie quotidienne**, **affaires**, **citoyenneté**, **loisirs** :

  * automatisation de **calculs fastidieux** ;
  * **circulation** d’informations (données, sons, images) entre **acteurs multiples et éloignés** ;
  * **tri/recherche** dans des **bases hétérogènes** ;
  * **objets “intelligents”** (voitures, fusées, maisons) ;
  * **télémédecine** (microchirurgie) ;
  * **régulation** des flux (trafic, production) ;
  * **mondes virtuels** (jeux, simulation).

### Questions structurantes

* Quelle **découverte essentielle** est au cœur de cette révolution ?
* Comment **mesurer** son importance et ses **conséquences sociales/culturelles** (actuelles, potentielles, prévisibles) ?

## Travail, production, formation

Fusion de **trois activités** :

1. **Production** (directe/indirecte)
2. **Recherche & Développement**
3. **Enseignement & communication des savoirs**

→ L’humain de demain : **producteur**, **créateur**, **apprenant-enseignant** tout au long de la vie.
→ Transformations majeures : **division du travail**, **responsabilités**, **qualifications**, **formation initiale & continue**.
→ **Gains de productivité** attendus.

## Conséquences sociales, culturelles, familiales

* Se préparer à une **société en réseau** ; la **dimension émancipatrice** devient stratégique.
* Apprendre à **vivre/créer/communiquer/collaborer** en **situations non hiérarchiques**.
* Développer **originalité**, **potentiel** et **richesses propres**.
* Quel **système politique, économique, social** saura mettre en œuvre cette révolution ?
* **William Morris** (design, utopiste anglais) imaginait une **société du loisir** (intuition encore actuelle).
* Pour certains, la société informationnelle pourrait **réaliser les idéaux des Lumières**, après la parenthèse de la révolution industrielle.

---

# recap

* **Théorie des automates** & **Intelligence artificielle**
* **Représentation des connaissances**, **modélisation**
* **Sémiotique**, **théorie du sens**
* **Systémique**, **théorie de l’autonomie**

---

# Théorie des automates

* Intimement liée à l’étude des **langages formels** (informatique théorique).
* Étude de la **puissance de calcul** de **divers modèles** (automates finis, etc.).
* Porte sur la **syntaxe** des **langages formels** et des **langues naturelles**, ainsi que sur la **calculabilité** (limites du calcul pour une machine donnée).

## Dates importantes

* **1937** : **Alan Turing** montre qu’un type particulier d’automate (**machine de Turing**) calcule tout ce que tout autre automate peut calculer, et qu’il est **impossible de faire mieux**.

  * **Machine de Turing universelle** : peut reproduire le **comportement de n’importe quelle machine de Turing** → l’ordinateur était né.
* **1956** : **Théorème de Kleene** — **équivalence** entre **graphes de transition**, **automates finis** et **grammaires régulières**.

---

# Machine de Turing — Intuition

* Composée d’une **partie de contrôle** (nombre **fini d’états** + **transitions**) et d’une **bande (théoriquement) infinie** de symboles, lue/écrite par une **tête de lecture/écriture**.
* **Abstraction** d’un ordinateur :

  * partie de contrôle → **microprocesseur** ;
  * bande → **mémoire** (centrale + externes) ;
  * tête → **bus** reliant processeur et mémoire.
* Différence avec l’ordinateur réel : la **mémoire** est **infinie** dans le modèle.

## Deux modes d’utilisation

* **Accepteur** : l’entrée est **acceptée** (oui) ou **rejetée** (non) → définit un **langage**.
* **Calculateur** : l’entrée est transformée en **sortie(s)** ; si unique, la machine **calcule une fonction**.

---

## Machine de Turing — Formalisation

Soit un **septuplet** :

$$
M = (Q, \Gamma, \Sigma, \delta, s, B, F)
$$

où :

* \$Q\$ : ensemble **fini** d’états
* \$\Gamma\$ : **alphabet du ruban**
* \$\Sigma \subseteq \Gamma\$ : **alphabet d’entrée**
* \$\delta : Q \times \Gamma \to Q \times \Gamma \times {L, R}\$ : **fonction (partielle) de transition** (*L* = Left, *R* = Right)
* \$s \in Q\$ : **état initial**
* \$B \in \Gamma - \Sigma\$ : **symbole blanc** (p. ex. `#`)
* \$F \subseteq Q\$ : **états terminaux** (accepteurs)

---
**COURS 2**

# Épistémologie — **Cours 2**

**Machine de Turing, épistémologie de l’informatique : constituants, représentations, limites**

**MASTER M1 (2025–2026) — « Information et Communication »**
**Prof. L. Devillers** — [devil@lisn.fr](mailto:devil@lisn.fr)

---

## 0) Rappels — Vocabulaire formel

| Terme               | Définition courte                                            |
| ------------------- | ------------------------------------------------------------ |
| **Configuration**   | État courant + contenu de bande + position de la tête.       |
| **Transition**      | Application δ qui met à jour (état, symbole, mouvement L/R). |
| **Bloqué**          | Aucune transition applicable : arrêt non acceptant.          |
| **Acceptation**     | La machine **atteint un état acceptant** et s’arrête.        |
| **Non-termination** | Suite infinie de transitions : ni acceptation ni rejet.      |

> En **TM non déterministe**, un mot est **accepté** s’il **existe au moins un calcul acceptant**.

---

## 1) MT — Exemple de calcul

```
Entrée:  a  b  b  a  #
Tête:    ^
État:    0
```

**Tableau minute (à remplir)**

| Étape | Config. | Raison           |
| ----- | ------- | ---------------- |
| 0     | …       | État initial     |
| 1     | …       | Application de δ |
| 2     | …       | …                |

---

## 2) Informatique comme science — Triangle I‑A‑M

```
Information  →  Algorithme  →  Machine
(encodage)      (méthode)      (exécution)
```

| Bloc            | Question clé       | Exemple                        |
| --------------- | ------------------ | ------------------------------ |
| **Information** | Comment encoder ?  | Texte en tokens, son en trames |
| **Algorithme**  | Quelle procédure ? | Décision, optimisation         |
| **Machine**     | Comment exécuter ? | CPU/GPU, mémoire               |

---

## 3) Gnoséologie — Double filiation

```
Formelle (maths, logique) ─┐
                          ├─► Informatique (science hybride)
Technologique (hard/soft) ─┘
```

| Gain               | Vigilance              |
| ------------------ | ---------------------- |
| Preuves, garanties | Hypothèses irréalistes |
| Réplicabilité      | Perte de contexte      |

---

## 4) Représentations — Embeddings & LVM

```
Texte ─► Enc. texte ──┐
                      ├─► Fusion ─► Tâche
Image ─► Enc. image ──┘
```

| Fusion  | Idée               | Remarque          |
| ------- | ------------------ | ----------------- |
| Précoce | Concaténer/aligner | Interaction forte |
| Tardive | Combiner décisions | Modulaire         |
| Hybride | Mixte              | Compromis         |

---

## 5) Théorie ↔ Expérimentation (boucle)

```
Maths ─► Modèles ─► Algorithmes ─► Systèmes
  ▲                               │
  └────────── retours ◄───────────┘
```

---

## 6) Atelier MT — Gabarits

**Notation** : `u [q, σ] v`

**Stratégies** : existence d’un calcul acceptant / cycle pour non‑terminaison.

---

## 7) Devoir — Mémoire (10 pages max)

```
1. Question & contexte
2. Cadre conceptuel
3. État de l’art
4. Étude de cas
5. Limites & pistes
6. Conclusion
7. Bibliographie
```

**barème**

| Axe          | Attendu               |
| ------------ | --------------------- |
| Clarté       | Problématique précise |
| Rigueur      | Définitions, sources  |
| Analyse      | Arguments, limites    |
| Éthique      | Risques & mesures     |
| Présentation | Forme & biblio        |

---

## 8) Résumé

```
Épistémologie appliquée
├─ TM : acceptation par existence d’un calcul
├─ I–A–M : science hybride
├─ Embeddings/LVM : atouts/limites
├─ Limites : décidabilité, complexité
└─ Éthique : biais, gouvernance
```
