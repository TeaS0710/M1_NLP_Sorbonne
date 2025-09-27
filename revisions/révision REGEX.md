# Cours de Révisions – Expressions Régulières (Regex)

## 1. Introduction
Les **expressions régulières** (regex) permettent de rechercher, filtrer et manipuler des chaînes de caractères grâce à des motifs décrivant un texte.

Elles sont utilisées dans de nombreux langages (Python, Java, JavaScript, Bash, etc.).

---

## 2. Bases des regex

### 2.1 Caractères simples
- `a` → correspond à la lettre **a**
- `abc` → correspond à la chaîne exacte **abc**

### 2.2 Métacaractères
- `.` → n’importe quel caractère (sauf retour à la ligne)
- `\.` → le caractère point `.`
- `\d` → chiffre `[0-9]`
- `\D` → tout sauf un chiffre
- `\w` → caractère alphanumérique + underscore `[a-zA-Z0-9_]`
- `\W` → tout sauf un caractère alphanumérique
- `\s` → espace, tabulation, retour ligne
- `\S` → tout sauf un espace

---

## 3. Classes de caractères
- `[abc]` → un seul caractère parmi `a`, `b` ou `c`
- `[^abc]` → un caractère qui **n’est pas** `a`, `b` ou `c`
- `[a-z]` → une lettre minuscule
- `[A-Z]` → une lettre majuscule
- `[0-9]` → un chiffre

Exemple :
- `[aeiou]` → une voyelle
- `[a-zA-Z0-9]` → un caractère alphanumérique

---

## 4. Quantificateurs
- `a*` → 0 ou plusieurs `a`
- `a+` → 1 ou plusieurs `a`
- `a?` → 0 ou 1 `a`
- `a{3}` → exactement 3 `a`
- `a{2,4}` → entre 2 et 4 `a`
- `a{2,}` → au moins 2 `a`

Exemple :
- `\d{4}` → exactement 4 chiffres (ex: année `2025`)

---

## 5. Groupes et alternatives
- `(abc)` → capture le groupe `abc`
- `(a|b)` → correspond à `a` **ou** `b`
- `(?:abc)` → groupe **non capturant**
- `\1`, `\2` → références aux groupes capturés

Exemple :
- `(ha)+` → `ha`, `hahaha`, `hahahaha`

---

## 6. Ancrages
- `^` → début de chaîne
- `$` → fin de chaîne
- `\b` → limite de mot
- `\B` → pas une limite de mot

Exemple :
- `^Bonjour` → commence par "Bonjour"
- `fin$` → se termine par "fin"
- `\bchat\b` → mot exact "chat"

---

## 7. Regexp avancées

### 7.1 Assertions (lookaround)
- `(?=...)` → lookahead positif (doit être suivi de)
- `(?!...)` → lookahead négatif (ne doit pas être suivi de)
- `(?<=...)` → lookbehind positif (doit être précédé de)
- `(?<!...)` → lookbehind négatif (ne doit pas être précédé de)

Exemples :
- `\d(?=€)` → chiffre suivi de "€"
- `\d(?!€)` → chiffre non suivi de "€"
- `(?<=\+)33` → `33` précédé de "+"
- `(?<!\+)33` → `33` non précédé de "+"

### 7.2 Modificateurs
- `i` → insensible à la casse
- `g` → recherche globale (JS)
- `m` → multi-lignes (`^` et `$` sur chaque ligne)
- `s` → le `.` inclut aussi les retours à la ligne

---

## 8. Exemples pratiques

1. **Email**
