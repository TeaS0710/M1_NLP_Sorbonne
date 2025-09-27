---

# Fiche de révision – Markdown

---

## 1. Introduction

* **Markdown** : langage léger pour formater du texte.
* Utilisé sur GitHub, forums, docs, notes (ex. : README.md).
* Lisible brut **et** rendu stylé.

---

## 2. Titres

```md
# Titre 1
## Titre 2
### Titre 3
#### Titre 4
```

-> Résultat :

# Titre 1

## Titre 2

### Titre 3

#### Titre 4

---

## 3. Texte

```md
Texte normal
**Gras**
*Italique*
***Gras + italique***
~~Barré~~
```

-> Résultat :
Texte normal
**Gras**
*Italique*
***Gras + italique***
~~Barré~~

---

## 4. Listes

### À puces

```md
- Pomme
- Banane
  - Kiwi
  - Orange
```

-> Résultat :

* Pomme
* Banane

  * Kiwi
  * Orange

### Numérotée

```md
1. Premier
2. Deuxième
3. Troisième
```

-> Résultat :

1. Premier
2. Deuxième
3. Troisième

---

## 5. Liens & images

```md
[Google](https://www.google.com)

![Texte alternatif](https://via.placeholder.com/150)
```

-> Résultat :
[Google](https://www.google.com)
![Texte alternatif](https://via.placeholder.com/150)

---

## 6. Citations

```md
> Ceci est une citation
>> Citation imbriquée
```

-> Résultat :

> Ceci est une citation
>
> > Citation imbriquée

---

## 7. Code

### Inline

```md
Voici du code : `print("Hello")`
```

-> Résultat :
Voici du code : `print("Hello")`

### Bloc

<pre>
```python
def carre(x):
    return x*x
```
</pre>

-> Résultat :

```python
def carre(x):
    return x*x
```

---

## 8. Tableaux

```md
| Nom     | Âge | Ville    |
|---------|-----|----------|
| Adrien  | 25  | Paris    |
| Marie   | 30  | Lyon     |
```

-> Résultat :

| Nom    | Âge | Ville |
| ------ | --- | ----- |
| Adrien | 25  | Paris |
| Marie  | 30  | Lyon  |

---

## 9. Séparateurs

```md
---
```

-> Résultat :

---

---

## 10. Checklists

```md
- [x] Terminé
- [ ] À faire
```

-> Résultat :

* [x] Terminé
* [ ] À faire

---

## 11. Liens internes (ancres)

```md
[Aller à la section Tables](#8-tableaux)
```

-> Clique pour descendre.

---

## 12. Notes de bas de page (selon moteur)

```md
Voici une note[^1].

[^1]: Explication de la note
```

---

## 13. Diagrammes (GitHub / extensions)

````md
```mermaid
graph TD;
  A-->B;
  B-->C;
````

````

-> Génère un schéma si pris en charge (GitHub, Obsidian).

---

## 14. Exemples pratiques
### README minimal
```md
# Mon Projet
Un projet en **Python**.

## Installation
```bash
pip install -r requirements.txt
````

## Usage

```bash
python main.py
```

```

---
