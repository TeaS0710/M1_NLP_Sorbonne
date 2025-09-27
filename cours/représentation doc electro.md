# Représentation et traitement des documents électroniques

**M1SOL041 — Master 1 « Langue et Informatique »**
2025–2026
**Enseignantes** : Ljudmila **PETKOVIC** / Samia **SBISSI ABDERRAHMAN**

---

## Modalités prévisionnelles

* **Calendrier** : du **16 septembre au 16 décembre 2025**
* **Durée** : CM (1h) + TD (1h30)
* **Évaluation** : contrôle continu + examen final (**50%**)

  * PETKOVIC : **1 contrôle (25%)**
  * ABDERRAHMAN : **TBD (25%)**

### Calendrier prévisionnel (PETKOVIC)

1. 16/09 : Fondamentaux XML
2. 23/09 : Dictionnaires électroniques en XML (DTD)
3. 30/09 : Base de données XML (XML Schema)
4. 07/10 : Interrogation (XPath/XQuery)
5. 14/10 : Transformation (XSLT, Python)
6. 21/10 : Contrôle continu
7. 27/10–02/11 : Vacances

---

# Notions fondamentales

## Documents électroniques

* Documents **structurés** (texte, image, son, vidéo…) représentés en **forme numérique**.
* Codage binaire interprétable par les systèmes informatiques.

## Formats de représentation

* **Format ouvert** vs **format fermé/propriétaire**
* **Format texte** : HTML, XML, XHTML, CSV, CSS…

## Interopérabilité

* Capacité d’échange et de réutilisation des données entre systèmes.
* Objectif : éviter problèmes de **compatibilité**, **compression**, **échange**.
* Formats communs et ouverts : **HTML, XML, JSON…**

### Standards

* **XML (1998)** : généralisation du HTML, principe de balisage.
* **JSON (2006)** : sous-ensemble de JavaScript, modèle hiérarchique en arbre.

---

# Historique

* **SGML** (Standard Generalized Markup Language) → ancêtre.
* **HTML** (HyperText Markup Language) : interprétable par navigateur web, standardisé.
* **XML** (eXtensible Markup Language) : recommandation du **W3C** (1998).

  * Séparation stricte : **contenu** / **mise en forme**.

---

# Langages de balisage

## Définition

Langage de formatage destiné à transformer un texte brut en **document structuré** en insérant des **marques procédurales** et **descriptives**.

## Types de balises

* **Balises en paires** : `<b> … </b>`
* **Balises auto-fermantes** : `<img />`

### Exemple

```xml
<livre>
  <titre>Le Mage du Kremlin</titre>
  <auteur>Giuliano da Empoli</auteur>
  <éditeur>Gallimard</éditeur>
  <année>2022</année>
</livre>
```

---

# XML et HTML

| **HTML**                | **XML**                                     |
| ----------------------- | ------------------------------------------- |
| Balises prédéfinies     | Balises nommage libre                       |
| Mélange contenu + forme | Séparation stricte fond (XML) / forme (CSS) |
| Utilisation web         | Utilisation large (BD, métadonnées…)        |

### Exemple comparatif

**HTML**

```html
<html>
  <head><title>Accueil</title></head>
  <body>
    <header><h1>Home</h1></header>
    <main><p>Bienvenue à Sorbonne Université.</p></main>
  </body>
</html>
```

**XML**

```xml
<site_sorbonne>
  <accueil>Home</accueil>
  <presentation>Bienvenue à Sorbonne Université</presentation>
</site_sorbonne>
```

---

# Structure d’un document XML

### Prologue

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
```

* Version XML (1.0 ou 1.1)
* Encodage (UTF-8 par défaut)
* Standalone : DTD interne (yes) ou externe (no)

### Corps du document

* **Élément racine** unique.
* **Imbrication stricte** des éléments (pas de chevauchement).

### Exemple

```xml
<mail>
  <de>Jean</de>
  <a>Marie</a>
</mail>
```

---

# Caractères spéciaux (escape characters)

* `>` → `&gt;` ou `&#62;`
* `<` → `&lt;` ou `&#60;`
* `&` → `&amp;` ou `&#38;`
* `'` → `&apos;` ou `&#39;`
* `"` → `&quot;` ou `&#34;`

---

# Éléments et attributs

## Élément

```xml
<name>Jean Dupont</name>
```

## Attribut

```xml
<cours date="03_mars_2023">Linguistique</cours>
```

* **Sous-élément** → structuration hiérarchique, volumétrie.
* **Attribut** → identifiant, méta-information.

---

# Modèle arborescent XML

* Document structuré sous forme **d’arbre hiérarchique**.
* **Racine** = nœud parent.
* **Éléments** = enfants.

---

# Niveaux de conformité

* **Bien formé** : respecte la syntaxe (balises, imbrication).
* **Valide** : bien formé + respecte une structure type (DTD, schéma XML).

---

# Technologies XML

* **DTD** : définition de type de document
* **XML Schema** : validation
* **XPath/XQuery** : interrogation
* **XSLT** : transformation
* **XLink/XPointer** : liens entre documents

---

# Métadonnées

## Définition

Informations structurées décrivant ou facilitant l’usage d’une ressource.

> *« Données sur les données »*.

### Types

* **Descriptives** : titre, auteur, format, droits d’accès…
* **Administratives** : gestion, conservation.
* **Structurelles** : organisation interne.

### Objectif

* Pérennité des données.
* Interopérabilité entre systèmes.
* Normalisation via standards (p. ex. **TEI** : Text Encoding Initiative).

---

# Outils

## Éditeurs

* Généralistes : Notepad++, Sublime Text
* Spécialisés : **Oxygen Editor**, Cooktop, Exchanger XML, Editix

## Validation

* [W3Schools XML Validator](https://www.w3schools.com/xml/xml_validator.asp)
* [Codebeautify XML Validator](https://codebeautify.org/xmlvalidator)

---

# Travaux dirigés

* **Questions de cours**
* **Cas pratique** : structuration d’un document XML à partir d’une page web

---

## tips

1. Respecter **indentation et imbrication**.
2. Déclarer **UTF-8** pour éviter les erreurs d’encodage.
3. Toujours ajouter un **prologue**.
4. Pas de chevauchement de balises.
5. Document = **bien formé** ≠ forcément **valide**.

---

## arbre

```
Représentation & traitement des docs électroniques
├─ Formats (ouvert/fermé ; texte/binaire)
├─ XML (syntaxe, validité, schémas)
├─ Outils (édition, validation, transformation)
├─ Interrogation (XPath/XQuery)
└─ Métadonnées (TEI, Dublin Core)
```

## Pipeline XML (du texte brut to rendu)

```
Source (texte) → Encodage XML → Validation (DTD/XSD)
     → Interrogation (XPath/XQuery) → Transformation (XSLT)
     → Sorties (HTML/PDF/JSON) → Archivage (XML natif/NoSQL)
```

## « ouvert vs fermé »

| Critère          | Format ouvert  | Format fermé  |
| ---------------- | -------------- | ------------- |
| Spécification    | Publique       | Propriétaire  |
| Interopérabilité | Forte          | Variable      |
| Pérennité        | Bonne          | Risquée       |
| Exemples         | XML, JSON, CSV | DOCX\*, PDF\* |

> \*Selon l’implémentation : certains contiennent des spécs publiques mais des extensions propriétaires.

## Bonnes pratiques « XML propre »

| Point       | À faire                   | À éviter                        |
| ----------- | ------------------------- | ------------------------------- |
| Encodage    | `UTF-8` déclaré           | Encodages mixtes                |
| Racine      | Unique                    | Éléments multiples au top-level |
| Nommage     | `kebab-case`/`snake_case` | Espaces, accents                |
| Attributs   | Métadonnées, IDs          | Stocker des sous-arbres         |
| Indentation | 2 ou 4 espaces            | Tabs mixtes                     |

## Gabarit DTD minimal

```dtd
<!-- fichier: livre.dtd -->
<!ELEMENT livre (titre, auteur+, editeur?, annee)>
<!ELEMENT titre (#PCDATA)>
<!ELEMENT auteur (#PCDATA)>
<!ELEMENT editeur (#PCDATA)>
<!ELEMENT annee (#PCDATA)>
```

**XML associé**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE livre SYSTEM "livre.dtd">
<livre>
  <titre>Exemple</titre>
  <auteur>Nom, Prénom</auteur>
  <annee>2025</annee>
</livre>
```

## Gabarit XML Schema (XSD) minimal

```xml
<!-- fichier: livre.xsd -->
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <xsd:element name="livre">
    <xsd:complexType>
      <xsd:sequence>
        <xsd:element name="titre" type="xsd:string"/>
        <xsd:element name="auteur" type="xsd:string" maxOccurs="unbounded"/>
        <xsd:element name="editeur" type="xsd:string" minOccurs="0"/>
        <xsd:element name="annee" type="xsd:gYear"/>
      </xsd:sequence>
    </xsd:complexType>
  </xsd:element>
</xsd:schema>
```

**XML associé**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<livre xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:noNamespaceSchemaLocation="livre.xsd">
  <titre>Exemple</titre>
  <auteur>Nom, Prénom</auteur>
  <annee>2025</annee>
</livre>
```

## XPath

| Besoin              | XPath                   |
| ------------------- | ----------------------- |
| Tous les titres     | `//titre/text()`        |
| Livres après 2010   | `//livre[annee > 2010]` |
| Auteur 1er          | `//livre/auteur[1]`     |
| Livres sans éditeur | `//livre[not(editeur)]` |

## XQuery (squelette minimal)

```xquery
(: fichier: livres.xq :)
for $l in doc("bibli.xml")//livre
where xs:integer($l/annee) >= 2010
order by $l/titre
return <item>{ $l/titre/text() }</item>
```

## XSLT (transformation XML → HTML minimal)

```xml
<!-- fichier: livre.xsl -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:template match="/">
    <html><body>
      <h1>Catalogue</h1>
      <ul>
        <xsl:for-each select="//livre">
          <li><xsl:value-of select="concat(titre, ' — ', annee)"/></li>
        </xsl:for-each>
      </ul>
    </body></html>
  </xsl:template>
</xsl:stylesheet>
```

## Modèle « Dataset/Corpus XML »

```
# Fiche corpus XML — [Nom]
Licence :
Schéma (DTD/XSD) :
Couverture : (domaines, langues)
Taille : (docs, tokens)
Qualité : (validation %, erreurs types)
Outillage : (XPath/XQuery/XSLT/Python)
Notes : (biais, limites)
```

## Kanban TD (à copier en README)

```
À faire
- Définir DTD/XSD sur mini-corpus
- Rédiger 10 documents bien formés
- Écrire 5 requêtes XPath utiles

En cours
- XSLT v1: listing HTML

Fait
- Prologue XML + encodage
```

## Check

**Bien formé**

* [ ] Prologue + encodage
* [ ] Élément racine unique
* [ ] Imbrication correcte
* [ ] Échappement des caractères spéciaux

**Valide (contre schéma)**

* [ ] DTD/XSD référencé
* [ ] Types conformes (`xsd:gYear`, etc.)
* [ ] Cardinalités respectées

## Schéma « arbre DOM »

```
Document
└─ livre
   ├─ titre : "Exemple"
   ├─ auteur : "Nom, Prénom"
   └─ annee : 2025
```

## Mini glossaire

| Terme      | Définition                        |
| ---------- | --------------------------------- |
| **DTD**    | Grammaire déclarative (structure) |
| **XSD**    | Schéma typé (XML Schema)          |
| **XPath**  | Sélecteurs de nœuds/valeurs       |
| **XQuery** | Langage de requêtes XML           |
| **XSLT**   | Transformation XML → autre format |
| **TEI**    | Norme XML pour les textes         |

## Script Python (lecture/validation simple)

```python
# lecture_xml.py (extrait)
from xml.etree import ElementTree as ET

root = ET.parse("livre.xml").getroot()
for titre in root.iter("titre"):
    print(titre.text)
```

> Astuce : pour la **validation XSD** en Python, préférer `lxml` (`XMLSchema`).

## Erreurs courantes

| Erreur                     | Symptôme           | Remède                      |
| -------------------------- | ------------------ | --------------------------- |
| Balise non fermée          | Parser error       | Vérifier l’imbrication      |
| Caractère non échappé      | `&` dans texte     | Remplacer par `&amp;`       |
| Multiples racines          | Document invalide  | Conserver une racine unique |
| Attributs pour sous-arbres | Perte de structure | Utiliser des éléments       |

---

# CM2 — Définition de type de document (DTD)

**UE : Représentation et traitement des documents électroniques — M1SOL041**
**Date** : 23/09/2025
**Basé sur** : Takrouni (2024), adapté de Carton (2015).

---

## 0) Objectifs du CM

* Comprendre le rôle d’une **DTD** (Document Type Definition) : grammaire d’un **XML** (noms d’éléments, ordre/hiérarchie, attributs).
* Savoir **lier** une DTD à un document (interne/externe).
* Déclarer **éléments**, **modèles de contenu** et **attributs** (types, valeurs par défaut).

```
XML valide = XML bien formé + conforme à la DTD
```

> *Bien formé* = règles de syntaxe XML (imbrication, fermetures). *Valide* = conforme à la DTD.

---

## 1) Notions essentielles

### 1.1 Définition

**DTD** : langage déclaratif (hérité de **SGML**) décrivant la **structure** d’un type de documents XML. La DTD **n’est pas** écrite en XML.

### 1.2 Liaison XML ↔ DTD

* **Interne** (dans le DOCTYPE du même fichier)
* **Externe** (fichier `.dtd` séparé, chemin relatif/absolu/URL)
* Possibilité de **combiner** interne + externe (les déclarations internes sont lues **en premier**).

**Formes usuelles**

```xml
<!-- Interne -->
<!DOCTYPE racine [
  <!-- déclarations DTD ici -->
]>

<!-- Externe (SYSTEM) -->
<!DOCTYPE personne SYSTEM "personne-1.dtd">
<personne>...</personne>

<!-- Externe (URL / absolu / relatif) -->
<!DOCTYPE personne SYSTEM "http://exemple.org/personne1.dtd">
<!DOCTYPE personne SYSTEM "E:/home/.../personne1.dtd">
<!DOCTYPE personne SYSTEM "personne-1.dtd">
```

---

## 2) Déclaration d’éléments — `<!ELEMENT ...>`

**Schéma général** :

```
<!ELEMENT NomElement (ModèleDeContenu)>
```

* Le **modèle** précise le **contenu** : sous‑éléments, texte `#PCDATA`, mixte, `EMPTY`, `ANY`.

### 2.1 Séquence, choix, cardinalités

| Construction       | Signification (compacte)      |        |                              |
| ------------------ | ----------------------------- | ------ | ---------------------------- |
| `elt1, elt2, elt3` | **Séquence** : dans cet ordre |        |                              |
| \`elt1             | elt2                          | elt3\` | **Choix exclusif** : un seul |
| `elt?`             | optionnel : 0 ou 1            |        |                              |
| `elt*`             | 0..n                          |        |                              |
| `elt+`             | 1..n                          |        |                              |
| `( ... )`          | **Parenthèses** pour combiner |        |                              |

**Ex.**

```dtd
<!ELEMENT nomElt (elt1+, (elt2 | elt3))>
```

### 2.2 Contenus textuels et mixtes

* **Texte seul** : `<!ELEMENT TEXTE (#PCDATA)>`
* **Mixte** : `<!ELEMENT MIXTE (#PCDATA | elt1 | elt2)*>`
  Règles : `#PCDATA` en **premier**, répété par `*` (obligatoire), adapté aux **textes narratifs**.

### 2.3 `ANY` et `EMPTY`

* `ANY` : contenu **libre** (utile pour essais de validation).
* `EMPTY` : contenu **vide** (ex. `<img .../>`).

---

## 3) Déclaration d’attributs — `<!ATTLIST ...>`

**Schéma général** :

```
<!ATTLIST NomElement
  nomAtt1 type1 defaut1
  nomAtt2 type2 defaut2
>
```
---

* Défauts : `#REQUIRED`, `#IMPLIED`, `#FIXED "val"`, ou valeur littérale **par défaut**.

### 3.1 Principaux types d’attributs

| Type        | Idée                                    |    |        |
| ----------- | --------------------------------------- | -- | ------ |
| `CDATA`     | chaîne libre                            |    |        |
| `ID`        | identifiant **unique** dans le document |    |        |
| `IDREF`     | **référence** vers un `ID` existant     |    |        |
| Énumération | valeurs limitées : \`(v1                | v2 | ...)\` |

*Exemples du cours* :

```dtd
<!ATTLIST livre ISBN ID #REQUIRED>
<!ATTLIST membre_projet chercheur IDREF #IMPLIED>
<!ATTLIST date mois (janvier|fevrier|mars) #REQUIRED>
```
---

## 4) Exemples fil rouge

### 4.1 Deux DTD minimales

```dtd
<!ELEMENT personne (identite, profession*)>
<!ELEMENT identite (nom, prenom+)>
<!ELEMENT nom (#PCDATA)>
<!ELEMENT prenom (#PCDATA)>
<!ELEMENT profession (#PCDATA)>
```

```dtd
<!ELEMENT livre (titre, chapitre+)>
<!ELEMENT titre (#PCDATA)>
<!ELEMENT chapitre (#PCDATA)>
```

### 4.2 DTD + XML avec attributs

```dtd
<!ELEMENT livre (auteur, format)>
<!ATTLIST livre id CDATA #REQUIRED
                 nbpages CDATA #REQUIRED
                 titre CDATA #REQUIRED>
<!ELEMENT auteur (nom, prenom)>
<!ELEMENT format (mesure+)>
<!ATTLIST format type CDATA #REQUIRED>
<!ELEMENT mesure (#PCDATA)>
<!ATTLIST mesure dim (hauteur|largeur|longueur) #REQUIRED
                 unite (cm|mm|in) #REQUIRED>
<!ELEMENT nom (#PCDATA)>
<!ELEMENT prenom (#PCDATA)>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE livre SYSTEM "exemple.dtd">
<livre id="561" nbpages="190" titre="La compagnie des spectres">
  <auteur>
    <nom>Salvayre</nom>
    <prenom>Lydie</prenom>
  </auteur>
  <format type="poche">
    <mesure dim="largeur" unite="cm">11</mesure>
    <mesure dim="longueur" unite="cm">19</mesure>
    <mesure dim="hauteur" unite="mm">10</mesure>
  </format>
</livre>
```

---

## 5) EXO — énoncés & solutions

**Énoncés**

1. Entrée + Plat + Dessert.
2. Entrée + Plat + (Fromage **ou** Dessert).
3. (Entrée + Plat) **ou** (Plat + Dessert).

**Solutions**

```dtd
<!DOCTYPE Menu [
<!ELEMENT Menu (Entree, Plat, Dessert)>
<!ELEMENT Entree (#PCDATA)>
<!ELEMENT Plat (#PCDATA)>
<!ELEMENT Dessert (#PCDATA)>
]>
```

```dtd
<!DOCTYPE Menu [
<!ELEMENT Menu (Entree, Plat, (Fromage | Dessert))>
<!ELEMENT Entree (#PCDATA)>
<!ELEMENT Plat (#PCDATA)>
<!ELEMENT Fromage (#PCDATA)>
<!ELEMENT Dessert (#PCDATA)>
]>
```

```dtd
<!DOCTYPE Menu [
<!ELEMENT Menu ((Entree, Plat) | (Plat, Dessert))>
<!ELEMENT Entree (#PCDATA)>
<!ELEMENT Plat (#PCDATA)>
<!ELEMENT Dessert (#PCDATA)>
]>
```

> Remarque : normaliser en noms d’éléments (`Entree`) pour éviter les soucis d’encodage.

---

## 6) checkup

* **En ligne** : W3Schools XML Validator ; Truugo (bien formé + DTD interne).
* **CLI** : `xmllint --noout --valid note.xml` ; `xmlstarlet val -d monfichier.dtd monfichier.xml`.
* **GUI** : XML Copy Editor ; *Oxygen XML Editor* (licence).

**Mini‑check list**

```
[ ] Document bien formé (imbrication, échappements)
[ ] DOCTYPE correct (interne/externe)
[ ] Types/occurrences conformes
[ ] Attributs (#REQUIRED/#IMPLIED/#FIXED) respectés
```

---

## 7) modèles de contenu (ASCII)

```
Séquence      : (A, B, C)
Choix         : (A | B | C)
Option        : A?
Répétition 0+ : A*
Répétition 1+ : A+
Texte         : (#PCDATA)
Mixte         : (#PCDATA | A | B | ...)*
Libre         : ANY
Vide          : EMPTY
```

**Rappel** : parenthèses pour combiner séquences/choix/cardinalités.

---

## 8) Modèles prêts à l’emploi

### 8.1 DTD interne (squelette)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Racine [
  <!ELEMENT Racine (Section+)>
  <!ELEMENT Section (Titre, Paragraphe*)>
  <!ELEMENT Titre (#PCDATA)>
  <!ELEMENT Paragraphe (#PCDATA)>
]>
<Racine>
  <Section>
    <Titre>Intro</Titre>
    <Paragraphe>…</Paragraphe>
  </Section>
</Racine>
```

### 8.2 DTD externe + chemin relatif

```xml
<!DOCTYPE corpus SYSTEM "corpus.dtd">
<corpus>…</corpus>
```

### 8.3 ATTLIST

```dtd
<!ATTLIST item id ID #REQUIRED>
<!ATTLIST lien ref IDREF #IMPLIED>
<!ATTLIST date mois (jan|fev|mar) #REQUIRED>
```

---

## 10) checkup de l'idiot

```
DTD = grammaire XML
├─ Déclarations d’éléments : séquence, choix, ?, *, +
├─ Contenus : #PCDATA, mixte, ANY, EMPTY
├─ Attributs : CDATA, ID, IDREF, énumérations
├─ Liaison : DOCTYPE interne/externe (SYSTEM)
└─ Validation : outils en ligne, CLI, éditeurs
```
