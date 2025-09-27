# 1) Installer & préparer

* **JDK** : installe un JDK (17 ou 21).
Eclipse → **Window > Preferences > Java > Installed JREs** → *Add…* → pointe vers le **JDK**, pas un simple JRE.
* **Nouveau workspace** : au premier lancement, accepte un dossier propre (ex. `~/workspace`).

# 2) Créer un projet “simple”

> Pour débuter, **évite Maven/Gradle et les modules**.

1. **File > New > Java Project**
2. **Project name** : `HelloEclipse`
3. *Décoche* “Create module-info.java” si proposé.
4. Finish.

Structure obtenue :

```
HelloEclipse
 └─ src/
    └─ (tes packages et classes iront ici)
 └─ JRE System Library [Java 17/21]
```

# 3) Packages & classes : règles de base

* **Package** = dossier logique. Nom en **minuscules** (ex. `com.exo.demo`).
* **Classe publique** : **1 seule** par fichier, et le **nom du fichier = nom de la classe** (ex. `Main.java` contient `public class Main`).
* La première ligne du fichier doit refléter le package :

  ```java
  package com.exo.demo;
  ```

  (et le fichier se trouve dans `src/com/exo/demo/`).
* **Méthode d’entrée** (exécutable) :

  ```java
  public static void main(String[] args) { ... }
  ```

# 4) Hello World (quick start)

1. **Right-click sur `src` > New > Package** → `com.exo.demo`
2. **Right-click sur le package > New > Class**

   * Name : `Main`
   * Coche **public static void main(String[] args)** → Finish
3. Colle/valide le code :

   ```java
   package com.exo.demo;

   public class Main {
       public static void main(String[] args) {
           System.out.println("Hello, Eclipse!");
       }
   }
   ```
4. **Run** : icône ▶️ verte, ou **Right-click > Run As > Java Application**.

# 5) Erreurs fréquentes (et fixes)

* **“Unresolved compilation problem”** : il y a des erreurs (marqueurs rouges). Ouvre le fichier, survole le rouge, corrige.
* **Deux classes `public` dans un fichier** : laisse **une seule** classe `public` et aligne le nom du fichier.
* **package mismatch** : le `package ...;` ne correspond pas au dossier → renomme le package ou déplace le fichier.
* **module-info.java gêne** : supprime `module-info.java` (Right-click > Delete) pour un projet simple.
* **Mauvais JRE/JDK** : Project > **Properties > Java Build Path** (ou **Project Facets/Compiler**) → assure **Java 17/21**.
* **Projet “bloqué”** : **Project > Clean…** puis relance **Build Automatically** (menu *Project*).

# 6) Raccourcis qui font gagner du temps

* **Ctrl+N** : nouveau fichier/élément
* **Ctrl+Space** : auto-complétion
* **Ctrl+Shift+F** : formater le code
* **Ctrl+/** : commenter/décommenter la ligne
* **Alt+Shift+R** : renommer (refactor)
* **F3** : aller à la déclaration
* **F11** : Debug (avec points d’arrêt à gauche de la marge)
