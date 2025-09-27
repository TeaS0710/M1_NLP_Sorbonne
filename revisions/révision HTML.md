---

# Fiche de révision – HTML

---

## 1. Introduction

* **HTML (HyperText Markup Language)** : structure des pages web.
* Fonctionne avec **CSS** (style) et **JavaScript** (interaction).
* Structure de base :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Ma page</title>
</head>
<body>
  <h1>Hello World</h1>
</body>
</html>
```

---

## 2. Titres & texte

```html
<h1>Titre 1</h1>
<h2>Titre 2</h2>
<p>Ceci est un paragraphe.</p>
<strong>Texte en gras</strong>
<em>Texte en italique</em>
<u>Texte souligné</u>
<br> <!-- Saut de ligne -->
<hr> <!-- Ligne horizontale -->
```

-> Résultat : un texte bien structuré avec titres, paragraphes, mise en forme.

---

## 3. Listes

### Liste à puces

```html
<ul>
  <li>Pomme</li>
  <li>Banane</li>
  <li>Orange</li>
</ul>
```

### Liste numérotée

```html
<ol>
  <li>Étape 1</li>
  <li>Étape 2</li>
</ol>
```

---

## 4. Liens & images

```html
<a href="https://www.google.com" target="_blank">Google</a>

<img src="https://via.placeholder.com/150" alt="Exemple d'image">
```

-> `target="_blank"` ouvre dans un nouvel onglet.

---

## 5. Tableaux

```html
<table border="1">
  <tr>
    <th>Nom</th>
    <th>Âge</th>
  </tr>
  <tr>
    <td>Adrien</td>
    <td>25</td>
  </tr>
  <tr>
    <td>Marie</td>
    <td>30</td>
  </tr>
</table>
```

---

## 6. Formulaires

```html
<form action="/traitement" method="post">
  <label>Nom : <input type="text" name="nom"></label><br>
  <input type="number" name="age" placeholder="Âge"><br>
  <input type="password" name="mdp" placeholder="Mot de passe"><br>
  <input type="checkbox" name="ok"> J’accepte<br>
  <input type="radio" name="genre" value="H"> Homme
  <input type="radio" name="genre" value="F"> Femme<br>
  <select name="ville">
    <option>Paris</option>
    <option>Lyon</option>
  </select><br>
  <input type="submit" value="Envoyer">
</form>
```

---

## 7. Structure sémantique (HTML5)

```html
<header>En-tête du site</header>
<nav>Menu</nav>
<main>Contenu principal</main>
<article>Article indépendant</article>
<section>Section</section>
<aside>Barre latérale</aside>
<footer>Pied de page</footer>
```

---

## 8. Multimédia

```html
<img src="chat.png" alt="Un chat" width="200">

<audio controls>
  <source src="musique.mp3" type="audio/mpeg">
  Votre navigateur ne supporte pas l’audio.
</audio>

<video controls width="300">
  <source src="video.mp4" type="video/mp4">
  Votre navigateur ne supporte pas la vidéo.
</video>
```

---

## 9. Liens internes (ancres)

```html
<a href="#bas">Aller en bas</a>

<p id="bas">Section du bas</p>
```

---

## 10. Métadonnées & SEO

```html
<head>
  <meta charset="UTF-8">
  <meta name="description" content="Description de la page">
  <meta name="author" content="Adrien">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ma Page</title>
</head>
```

---

## 11. Exemple complet

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Exemple complet</title>
</head>
<body>
  <header>
    <h1>Mon Site</h1>
    <nav>
      <a href="#section1">Section 1</a> |
      <a href="#section2">Section 2</a>
    </nav>
  </header>

  <main>
    <section id="section1">
      <h2>Section 1</h2>
      <p>Ceci est un texte avec une <a href="https://www.google.com">lien</a>.</p>
    </section>

    <section id="section2">
      <h2>Section 2</h2>
      <img src="https://via.placeholder.com/100" alt="Exemple">
    </section>
  </main>

  <footer>
    <p>&copy; 2025 Adrien</p>
  </footer>
</body>
</html>
```

---
