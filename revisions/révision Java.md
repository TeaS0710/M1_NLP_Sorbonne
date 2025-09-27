---

# Fiche de révision – Java

---

## 1. Introduction

* **Java** : langage orienté objet, portable (JVM), typé statiquement.
* Compilation & exécution :

```bash
javac Main.java    # Compile
java Main          # Exécute
```

---

## 2. Structure minimale

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
```

* Tout doit être dans une **classe**.
* `main()` est le point d’entrée.

---

## 3. Variables & types

```java
int age = 20;          // Entier
double pi = 3.14;      // Réel
char lettre = 'A';     // Caractère
String nom = "Adrien"; // Chaîne
boolean vivant = true; // Booléen
```

**Constantes** :

```java
final int VITESSE = 120;
```

---

## 4. Entrées / sorties

```java
import java.util.Scanner;

Scanner sc = new Scanner(System.in);
System.out.print("Nom ? ");
String nom = sc.nextLine();
System.out.println("Bonjour " + nom);
```

---

## 5. Opérateurs

* Arithmétiques : `+ - * / %`
* Comparaison : `== != < > <= >=`
* Logiques : `&& || !`
* Affectation : `= += -= *= /=`

```java
int a = 10, b = 3;
System.out.println(a+b);   // 13
System.out.println(a/b);   // 3
System.out.println(a>b);   // true
```

---

## 6. Conditions

```java
if (age >= 18) {
    System.out.println("Majeur");
} else {
    System.out.println("Mineur");
}
```

Switch (Java 14+ possible avec flèches) :

```java
int choix = 2;
switch (choix) {
    case 1 -> System.out.println("Option 1");
    case 2 -> System.out.println("Option 2");
    default -> System.out.println("Invalide");
}
```

---

## 7. Boucles

```java
// For
for (int i=0; i<5; i++) {
    System.out.println("i=" + i);
}

// While
int n = 0;
while (n < 3) {
    System.out.println(n);
    n++;
}

// Do...while
int x = 5;
do {
    System.out.println(x);
    x--;
} while (x > 0);
```

---

## 8. Méthodes (fonctions)

```java
public static int carre(int n) {
    return n * n;
}

public static void main(String[] args) {
    System.out.println(carre(4));  // 16
}
```

---

## 9. Tableaux & chaînes

```java
int[] notes = {12, 15, 18};
System.out.println(notes[0]);  // 12

String mot = "Bonjour";
System.out.println(mot.length());   // 7
System.out.println(mot.toUpperCase()); // BONJOUR
```

---

## 10. Classes & objets

```java
class Voiture {
    private String marque;
    private int vitesse;

    public Voiture(String m, int v) {
        marque = m;
        vitesse = v;
    }

    public void accelerer() { vitesse += 10; }
    public void afficher() {
        System.out.println(marque + " : " + vitesse + " km/h");
    }
}

public class Main {
    public static void main(String[] args) {
        Voiture v1 = new Voiture("BMW", 120);
        v1.accelerer();
        v1.afficher();  // BMW : 130 km/h
    }
}
```

---

## 11. Héritage

```java
class Animal {
    public void parler() {
        System.out.println("Je suis un animal");
    }
}

class Chien extends Animal {
    @Override
    public void parler() {
        System.out.println("Wouf!");
    }
}

public class Main {
    public static void main(String[] args) {
        Chien c = new Chien();
        c.parler(); // Wouf!
    }
}
```

---

## 12. Interfaces

```java
interface Volant {
    void voler();
}

class Oiseau implements Volant {
    public void voler() {
        System.out.println("Je vole !");
    }
}
```

---

## 13. Collections

```java
import java.util.*;

ArrayList<String> liste = new ArrayList<>();
liste.add("pomme");
liste.add("banane");

for (String s : liste) {
    System.out.println(s);
}

HashMap<String, Integer> ages = new HashMap<>();
ages.put("Adrien", 25);
ages.put("Marie", 30);
System.out.println(ages.get("Adrien"));  // 25
```

---

## 14. Exceptions

```java
try {
    int x = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Erreur : " + e.getMessage());
} finally {
    System.out.println("Toujours exécuté");
}
```

---

## 15. Fichiers

```java
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        FileWriter fw = new FileWriter("test.txt");
        fw.write("Hello fichier");
        fw.close();
    }
}
```

---

## 16. Threads (bases)

```java
class MonThread extends Thread {
    public void run() {
        System.out.println("Thread en cours...");
    }
}

public class Main {
    public static void main(String[] args) {
        MonThread t = new MonThread();
        t.start();
    }
}
```

---

## 17. Exemple complet

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> nums = new ArrayList<>(Arrays.asList(5, 1, 8, 3));
        Collections.sort(nums);
        for (int n : nums) {
            System.out.print(n + " ");   // 1 3 5 8
        }
    }
}
```

---
