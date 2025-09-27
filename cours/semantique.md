### Adrien Wasian Monkey

# SÉMANTIQUE COMPUTATIONNELLE

*M1SOL0505202*

> **Notions** : Modéliser, représenter et calculer le **sens** (mots, phrases, textes)
> au moyen de logiques, graphes de connaissances et méthodes statistiques/
> neuronales, afin de permettre l’inférence, la recherche sémantique et
> l’interopérabilité des connaissances.

---

## 1) Objectifs, périmètre, exemples

**Objectif.** Représentation **non ambiguë** du sens + **calcul** (inférence, requêtes,
vérification de contraintes).

**Périmètre.** Mots, syntagmes, phrases, textes ; concepts, relations, événements ;
connaissances générales et spécialisées.

**Exemple de passage NL → logique.**
NL : « Tous les chats sont des mammifères. »
FOL : ∀x (Chat(x) → Mammifère(x))
Fait : Chat(Siamois) → **Inférence** : Mammifère(Siamois)

---

## 2) Définitions

* **Langage naturel** : énoncés humains avec ambiguïtés et dépendance au contexte.
* **Sens** : contenu interprétable (référence, vérité, présupposés).
* **Représentation** : logique, RDF/OWL, cadres sémantiques, vecteurs/embeddings.
* **Formalisation** : passage à une forme **calculable** (FOL, RDF/OWL).
* **Calcul sémantique** : inférence, alignement, requêtes, vérifications.
* **Moteur d’inférence** : application de règles pour déduire de nouveaux faits.
* **Graphe de connaissances** : triplets + schéma (ontologie).
* **Ontologie** : classes, propriétés, axiomes (OWL).
* **WSD** : désambiguïsation lexicale par le contexte.
* **Distributionnalité** : “un mot se connaît par ses compagnons d’usage”.
* **Web sémantique** : publication/liaison de données (RDF/OWL/SPARQL).

---

## 3) Trois piliers : Source → Représentation → Calcul

| Pilier            | Exemple                                      |
| ----------------- | -------------------------------------------- |
| **Source**        | « Les loups vivent en meute. »               |
| **Formalisation** | ∀x (Loup(x) → VitEnMeute(x))                 |
| **Calcul**        | De *Loup(Akela)* déduire *VitEnMeute(Akela)* |

**Arbre (vue d’ensemble).**

```
Sens (objectif)
├─ Source : phrases, textes, contexte
├─ Représentation : FOL | RDF/OWL | cadres | vecteurs
└─ Calcul : inférence | requêtes | vérification
```

---

## 4) Inférence (règles → faits → conclusions)

**Ex. 1**

* Règle : ∀x (Lion(x) → Carnivore(x))
* Fait : Lion(Simba)
* Conclusion : **Carnivore(Simba)**

**Ex. 2 (chaînage)**

* R1 : Loup(x) → VitEnMeute(x)
* R2 : VitEnMeute(x) → Coopère(x)
* Fait : Loup(Akela)
* Conclusion : **Coopère(Akela)**

**Arbre (chaînage).**

```
Loup(Akela)
└─(R1)→ VitEnMeute(Akela)
          └─(R2)→ Coopère(Akela)
```

---

## 5) Deux approches (texte ↔ connaissances)

| Axe                       | Quand                            |
| ------------------------- | -------------------------------- |
| **Texte → Connaissances** | Beaucoup de texte, schéma limité |
| **Connaissances → Texte** | Ontologie riche, peu de données  |

*Méthodes (aperçu).* NER/RE, SRL, parsers, WSD, embeddings ↔
alignement d’entités, contraintes OWL, requêtes SPARQL.

**Arbre (choix d’approche).**

```
Analyse sémantique
├─ Texte → Connaissances (extraction)
└─ Connaissances → Texte (guidage par ontologie)
```

---

## 6) Paradigmes en sémantique

| Type           | + / – (condensé)                                      |
| -------------- | ----------------------------------------------------- |
| **Symbolique** | + explicable, rigoureux ; – gère mal flou/variabilité |
| **Neuronal**   | + robuste, performant ; – exige beaucoup de données   |
| **Hybride**    | + combine les atouts ; – intégration plus complexe    |

---

## 7) Représentations formelles

**7.1 Logique du premier ordre (FOL)**
Syntaxe : constantes, prédicats, connecteurs (¬ ∧ ∨ →), quantificateurs (∀, ∃).
Sémantique : vérité dans un modèle.
Raisonnement : déduction, unification, résolution.

**7.2 RDF / RDFS / OWL / SPARQL**
RDF : triplets *(s, p, o)*.
RDFS : hiérarchies de classes/propriétés.
OWL : contraintes (cardinalités, disjointesses, restrictions).
SPARQL : requêtes sur graphes.

*Exemple (RDFS).*
`:Siamois rdf:type :Chat .`
`:Chat rdfs:subClassOf :Mammifere .`
⇒ `:Siamois rdf:type :Mammifere .`

**Arbre (taxonomie simplifiée).**

```
Animal
└─ Mammifère
   └─ Félidé
      └─ Chat
         └─ Siamois
```

---

## 8) Wikipedia & DBpedia (et proches)

| Ressource     | Usage                                          |
| ------------- | ---------------------------------------------- |
| **Wikipedia** | Texte + infobox (source brute)                 |
| **DBpedia**   | Extraction RDF interrogeable (SPARQL)          |
| **Wikidata**  | Base éditée, multilingue, identifiants stables |

*SPARQL (exemple d’idée).*

```sparql
SELECT ?animal WHERE {
  ?animal rdf:type dbo:Mammal .
  ?animal dbo:family dbr:Felidae .
}
```

---

## 9) Applications

| Domaine          | Tâches (exemples)                          |
| ---------------- | ------------------------------------------ |
| Dialogue         | Intentions, suivi de contexte, anaphores   |
| Traduction       | Rôles sémantiques, désambiguïsation        |
| Recherche        | Concepts, expansion, indexation sémantique |
| Web sémantique   | Données liées, inférence OWL               |
| Systèmes experts | Règles métier, conformité                  |
| IE & QA          | Entités/relations/événements, Q/R logique  |

---

## 10) Ambiguïtés & contexte

| Type              | Exemple / Stratégie                     |
| ----------------- | --------------------------------------- |
| **Lexicale**      | « banque » — WSD + contexte             |
| **Structurale**   | attache prépositionnelle — parsing, SRL |
| **Référentielle** | anaphores — coréférence                 |
| **Pragmatique**   | implicatures — modèles de discours      |

---

## 11) Déduction / Abduction / Induction

| Type          | But                                              |
| ------------- | ------------------------------------------------ |
| **Déduction** | conclusions nécessaires à partir de règles/faits |
| **Abduction** | meilleure explication d’une observation          |
| **Induction** | généralisation à partir d’exemples               |

---

## 12) Pipeline « Texte → Connaissances »

1. Prétraitement (tokenisation, POS, lemmatisation)
2. Analyse en dépendances / constituants
3. Rôles sémantiques (SRL)
4. NER + *entity linking*
5. Extraction de relations/événements
6. Mapping vers RDF/OWL (alignement ontologique)
7. Requêtes/Inférence/QA

**Arbre (pipeline).**

```
Texte
└─ Prétraitement
   └─ Analyse syntaxique
      └─ SRL
         └─ NER & Linking
            └─ RE/EE
               └─ RDF/OWL (mapping)
                  └─ Requêtes & Inférence
```

---

## 13) Comparatif

| Critère         | Symbolique | Neuronal    | Hybride    |
| --------------- | ---------- | ----------- | ---------- |
| Données         | Faible     | Massive     | Mixte      |
| Explicabilité   | Haute      | Faible–Moy. | Moy.–Haute |
| Robustesse      | Moy.       | Haute       | Haute      |
| Rigueur logique | Haute      | Variable    | Haute      |
| Scalabilité     | Variable   | Bonne       | Variable   |

---

## 14) Méthode

1. Besoins & questions cibles
2. Représentation (OWL/FOL vs représentations vectorielles vs hybride)
3. Ontologie (réutilisable si possible)
4. Chaîne de traitement (IE → KG → inférence / récupération appuyée par connaissances)
5. Évaluation (extraction, inférence, ambiguïtés)
6. Itérations (règles, ontologie, linking, WSD)

---

## 15) Exercices

1. Exceptions. « Tous les oiseaux volent » ; « Les manchots sont des oiseaux » ;
   « Les manchots ne volent pas ».
   → Modéliser avec disjointesses/restrictions (OWL) **ou** logique non monotone.
2. SPARQL. Lister des félins non domestiques (filtrer sur la propriété adéquate).
3. WSD « batterie ». Indices pour distinguer *musique* vs *électronique*.
4. Chaînage. `Vivant∧Mammifère→RespireAir`, `Dauphin(Dolly)∧Mammifère(Dolly)` → **RespireAir(Dolly)**.

---

## 16) Chronologie (repères)

| Période   | Points clés                                                                             |
| --------- | --------------------------------------------------------------------------------------- |
| 1970–1990 | Symbolique, Prolog, systèmes experts                                                    |
| 1990–2000 | Lexiques structurés (WordNet), IE statistique                                           |
| 2000–2015 | Web sémantique (RDF/OWL/SPARQL), DBpedia/Wikidata                                       |
| 2015–2020 | Représentations contextuelles (ELMo/BERT)                                               |
| 2020–…    | Combinaisons neurales/symboliques, graphes + récupération, vérification des contraintes |

---

## 17) Études de cas

* **Contraintes de données** : cardinalités OWL (« tout *Contrat* relie ≥ 1 *Partie* ») → détection d’anomalies.
* **Question-Réponse sémantique** : requêtes SPARQL + axiomes → réponses vérifiables.
* **Dialogue réglementé** : interprétation linguistique + règles décisionnelles, traces d’inférence.

---

## 18) Bonnes pratiques & pièges

| Thème        | À faire / À éviter                                             |
| ------------ | -------------------------------------------------------------- |
| Ontologie    | construire petit, itérer / éviter la sur-modélisation          |
| IE/Linking   | normaliser + seuils / ne pas ignorer l’ambiguïté               |
| Raisonnement | tester sur cas réels / éviter règles contradictoires           |
| Hybride      | interface claire entre composantes / ne pas inventer le schéma |
| Évaluation   | jeux de test avec ambiguïtés / éviter une métrique unique      |

---

## 19) Annexes

**Rappels d’inférence.** Modus ponens ; syllogismes catégoriques.
**Triplet RDF.** Sujet — Prédicat — Objet.
**Axiomes OWL (courants).** `SubClassOf`, `EquivalentClass`, `DisjointClasses`,
domaines/ranges, cardinalités.

---

## 20) Récap

**20.1 Phrase → Logique**

| NL                     | FOL                         |
| ---------------------- | --------------------------- |
| « Chats → mammifères » | ∀x (Chat(x) → Mammifère(x)) |
| « Siamois est chat »   | Chat(Siamois)               |
| **Conclusion**         | Mammifère(Siamois)          |

**20.2 Chaînage**

| Règle/Fait               | Résultat       |
| ------------------------ | -------------- |
| Loup→Meute ; Loup(Akela) | Meute(Akela)   |
| Meute→Coopère            | Coopère(Akela) |

**20.3 Paradigmes**

| Type       | Outils (ex.)            |
| ---------- | ----------------------- |
| Symbolique | OWL, Prolog             |
| Neuronal   | BERT, modèles de langue |
| Hybride    | Graphes + inférence     |

---

## 21) Liste de projet

* [ ] Questions cibles
* [ ] Ontologie initiale/réutilisée
* [ ] NER/RE/Linking définis
* [ ] Stockage (RDF store/graph DB) + reasoner
* [ ] Évaluation (benchmarks + cas d’ambiguïtés)
* [ ] Interface entre modules (échange de formats)
* [ ] Traces d’inférence / explicabilité

---

## 22) Révisions

FOL & résolution • Description Logics (TBox/ABox) • SPARQL avancé •
WSD/SRL (SemCor, PropBank/FrameNet) • Combinaisons neurales/symboliques •
Graphes + récupération/conformité.
