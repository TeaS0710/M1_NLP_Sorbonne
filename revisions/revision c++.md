---

# Fiche de révision – C++

---

## 1. Introduction

* **C++** : langage compilé, orienté objet et performant.
* Utilisé pour systèmes, jeux vidéo, finance, IA, etc.
* Compilation :

  ```bash
  g++ prog.cpp -o prog    # Compile
  ./prog                  # Exécute
  ```

---

## 2. Structure minimale

```cpp
#include <iostream>      // Bibliothèque pour cout/cin
using namespace std;     // Évite d’écrire std:: à chaque fois

int main() {
    cout << "Hello World!" << endl;
    return 0;            // 0 = succès
}
```

---

## 3. Variables & types

```cpp
int age = 20;           // Entier
float pi = 3.14f;       // Réel simple précision
double grand = 2.71828; // Réel double précision
char lettre = 'A';      // Caractère
string nom = "Adrien";  // Chaîne de caractères
bool vivant = true;     // Booléen
```

**Constantes** :

```cpp
const int VITESSE = 120;
```

---

## 4. Entrées / sorties

```cpp
int x;
cout << "Donne un nombre : ";
cin >> x;
cout << "Tu as tapé : " << x << endl;
```

---

## 5. Opérateurs

* **Arithmétiques** : `+ - * / %`
* **Logiques** : `&& || !`
* **Comparaison** : `== != < > <= >=`
* **Affectation** : `= += -= *= /=`

Exemple :

```cpp
int a=10, b=3;
cout << a+b << endl;  // 13
cout << a/b << endl;  // 3 (division entière)
cout << (a>b) << endl; // 1 (true)
```

---

## 6. Conditions

```cpp
if (age >= 18) {
    cout << "Majeur" << endl;
} else {
    cout << "Mineur" << endl;
}
```

Switch :

```cpp
int choix=2;
switch(choix) {
    case 1: cout << "Option 1"; break;
    case 2: cout << "Option 2"; break;
    default: cout << "Invalide";
}
```

---

## 7. Boucles

```cpp
// For
for (int i=0; i<5; i++) {
    cout << "i=" << i << endl;
}

// While
int n=0;
while (n<3) {
    cout << n << endl;
    n++;
}

// Do...while
int x=5;
do {
    cout << x << endl;
    x--;
} while (x>0);
```

---

## 8. Fonctions

```cpp
int carre(int n) {
    return n*n;
}

int main() {
    cout << carre(4);   // 16
}
```

**Surcharge** :

```cpp
int add(int a, int b) { return a+b; }
double add(double a, double b) { return a+b; }
```

---

## 9. Tableaux & chaînes

```cpp
int notes[3] = {12, 15, 18};
cout << notes[0] << endl;   // 12

string mot = "Bonjour";
cout << mot.size() << endl; // 7
```

---

## 10. Pointeurs & références

```cpp
int x = 10;
int* p = &x;           // p contient l’adresse de x
cout << *p << endl;    // Affiche 10

int& ref = x;          // ref est une référence à x
ref = 20;
cout << x << endl;     // 20
```

---

## 11. Structures & classes

### Structure

```cpp
struct Point {
    int x, y;
};

Point p = {3, 4};
cout << p.x << " " << p.y;
```

### Classe

```cpp
class Voiture {
private:
    string marque;
    int vitesse;
public:
    Voiture(string m, int v) { marque=m; vitesse=v; }
    void accelerer() { vitesse += 10; }
    void afficher() { cout << marque << " : " << vitesse << " km/h"; }
};

int main() {
    Voiture v1("BMW", 120);
    v1.accelerer();
    v1.afficher();
}
```

---

## 12. Héritage

```cpp
class Animal {
public:
    void parler() { cout << "Je suis un animal"; }
};

class Chien : public Animal {
public:
    void parler() { cout << "Wouf!"; }
};

int main() {
    Chien c;
    c.parler();    // Wouf!
}
```

---

## 13. Vecteurs & STL

```cpp
#include <vector>
#include <algorithm>

vector<int> v = {4, 2, 7};
v.push_back(10);

sort(v.begin(), v.end());   // Trie
for (int n : v) cout << n << " ";  // 2 4 7 10
```

---

## 14. Gestion mémoire

```cpp
int* p = new int(42);  // Allocation
cout << *p << endl;    // 42
delete p;              // Libération
```

---

## 15. Exceptions

```cpp
try {
    throw runtime_error("Erreur grave");
} catch (exception& e) {
    cout << "Exception : " << e.what();
}
```

---

## 16. Exemple complet

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> nums = {5, 1, 8, 3};
    sort(nums.begin(), nums.end());
    for (int n : nums) cout << n << " ";
    return 0;
}
```

---
