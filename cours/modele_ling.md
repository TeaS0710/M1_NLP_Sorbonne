# Modèles de Linguistique Computationnelle

**CM1 — Expressions régulières**
*Nour El Houda Ben Chaabene*
[nour-el-houda.ben\_chaabene@sorbonne-universite.fr](mailto:nour-el-houda.ben_chaabene@sorbonne-universite.fr)
📍 Sorbonne Université — Master Langue et Informatique (2025–2026)

---

## Plan du cours

1. Définition et usages
2. Symboles fondamentaux
3. Quantificateurs
4. Groupes, alternatives, classes spéciales
5. Assertions (contexte)
6. Applications modernes
7. Bonnes pratiques et limites
8. Références

---

## 1. Définition

Une **expression régulière** (*regex*) est une formule textuelle décrivant un ensemble de chaînes.

Elle sert à :

* chercher,
* valider,
* extraire,
* ou transformer du texte selon des motifs précis.

-> Idée clé : mélange de **caractères ordinaires** et de **métacaractères** :

```
. ^ $ [ ] ( ) * + ? |
```

---

## 2. Usages principaux

### (1) Recherche

Texte : « Marie aime Paris et rome. »
Motif : `\b[A-Z][a-z]+\b`

Résultats :

* ✓ « Marie »
* ✓ « Paris »
* ✗ « rome »

> `\b` = frontière de mot ; `[A-Z]` = majuscule ; `[a-z]+` = une ou plusieurs minuscules.

---

### (2) Validation

Texte : « 75005 », « 34A00 »
Motif : `^\d{5}$`

Résultats :

* ✓ « 75005 »
* ✗ « 34A00 »

> `^` = début ; `\d{5}` = 5 chiffres ; `$` = fin.

---

### (3) Extraction

Texte : « Mon courriel est [prof.sorbonne@univ.fr](mailto:prof.sorbonne@univ.fr) »
Motif : `[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}`

Résultat :

* ✓ « [prof.sorbonne@univ.fr](mailto:prof.sorbonne@univ.fr) »

> Structure : partie locale + `@` + domaine + extension.

---

### (4) Nettoyage

Texte : « Tel : 01-45-67-89-10 »
Opération : remplacer `[- ]` par vide.
Résultat : `0145678910`

---

## 3. Symboles fondamentaux

### Point (joker)

Motif : `a.c`

* ✓ `abc`, `a9c`, `a c`
* ✗ `ac`

-> Pour chercher un vrai point : `a\.c`

---

### Ancrages

* Début : `^mot`
* Fin : `fin$`

Exemples :

* ✓ « mot », ✓ « motivation » (commence par "mot")
* ✗ « la fin » (ne commence pas par "mot")
* ✓ « la fin » (se termine par "fin")
* ✗ « finir » (ne se termine pas par "fin")

---

### Classes de caractères

* `[abc]` → ✓ « a », ✓ « b », ✗ « z »
* `[0-9]` → ✓ « 3 »
* `[^0-9]` → ✓ « a », ✗ « 3 »

---

## 4. Quantificateurs

### `*`, `+`, `?`

Texte : « ac », « abc », « abbc »

* `ab*c` → ✓ « ac », ✓ « abc », ✓ « abbc »
* `ab+c` → ✗ « ac », ✓ « abc », ✓ « abbc »
* `ab?c` → ✓ « ac », ✓ « abc », ✗ « abbc »

-> `*` = 0 ou + ; `+` = 1 ou + ; `?` = 0 ou 1.

---

### Bornes `{m,n}`

Texte : « aa », « aaa », « aaaa », « aaaaa »

* `a{3}` → ✓ « aaa », ✗ « aa », ✗ « aaaa »
* `a{2,4}` → ✓ « aa », ✓ « aaa », ✓ « aaaa », ✗ « aaaaa »

Usages typiques :

* Années : `\d{4}`
* Codes : `[A-Z0-9]{8}`

---

## 5. Groupes et alternatives

Texte : « chat », « chien », « cheval »

* `(chat|chien)` → ✓ « chat », ✓ « chien »
* `che(v|f)al` → ✓ « cheval », ✓ « chefal »

-> Les groupes servent aussi à capturer des sous-parties.

---

## 6. Classes spéciales et raccourcis

* `\d` → chiffre (0–9)
* `\D` → non-chiffre
* `\s` → espace, tab, retour ligne
* `\S` → non-espace
* `\w` → lettre/chiffre/underscore
* `\W` → non-`\w`
* `\b` → frontière de mot

**Exemples :**

* `\banti\b` → ✓ « anti », ✗ « antidote »
* Texte : « Il a 25 ans » → `\d+` → ✓ « 25 »

---

## 7. Assertions (contexte)

* `(?=x)` → suivi de `x`
* `(?!x)` → pas suivi de `x`
* `(?<=x)` → précédé de `x`
* `(?<!x)` → pas précédé de `x`

**Exemple** : texte « 100€ », « 200 \$ »

* Motif : `\d+(?=€)` → ✓ « 100 », ✗ « 200 »

---

## 8. Applications modernes

### Courriels (simplifié)

Motif :

```
^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$
```

> Conforme à un usage courant, pas à tous les cas RFC 5322.

---

### Dates ISO (AAAA-MM-JJ)

* Recherche simple : `\d{4}-\d{2}-\d{2}`
* Validation stricte :

```
^\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$
```

> La regex contrôle la **forme**, pas la validité calendrier (ex. 29 février, 30/31 jours).

Astuce : normaliser d’abord les séparateurs (`[/.]` → `-`).

---

### Réseaux sociaux

* Mentions : `@\w+`
* Hashtags : `#\w+`
* URL : `https?://\S+`

Exemple :
Texte : « Merci @Aline pour le lien [https://exemple.fr/page](https://exemple.fr/page) (voir #Cours) »
Résultats : ✓ `@Aline`, ✓ `#Cours`, ✓ `https://exemple.fr/page`

---

## 9. Bonnes pratiques

* **Ancrer** avec `^...$` pour la validation stricte.
* **Échapper** les métacaractères (`\.`, `\[`, `\]`, `\(`, `\)`, `\?`, etc.).
* **Quantifier avec parcimonie** :

  * Préférer `[A-Za-z]{2,4}` à `[A-Za-z]+` si on connaît les bornes.
* **Tester** sur des cas variés (vrais/faux positifs, faux négatifs).
* **Documenter** les motifs longs avec exemples.
* **Préférer la lisibilité** à l’efficacité brute ou aux « attrape-tout ».

---

## 10. Limites et alternatives

* **Structures riches** (HTML, JSON, XML) → utiliser un parseur dédié.
* **Cas particuliers** : espaces insécables, accents, encodages → normalisation préalable.
* **Bon réflexe** : combiner regex + bibliothèques spécialisées (dates, mails, URLs).

---

## 11. Références utiles

* [Python `re`](https://docs.python.org/3/library/re.html)
* [HOWTO Regex](https://docs.python.org/3/howto/regex.html)
* [RFC 5322 — Email](https://datatracker.ietf.org/doc/html/rfc5322)
* [Unicode Emoji](https://unicode.org/emoji/charts/full-emoji-list.html)
* [W3C XML Schema Regex](https://www.w3.org/TR/xmlschema-2/)
* [regex101 — testeur en ligne](https://regex101.com)
* Jurafsky & Martin (2023), *Speech and Language Processing* : [SLP3](https://web.stanford.edu/~jurafsky/slp3/)

---
