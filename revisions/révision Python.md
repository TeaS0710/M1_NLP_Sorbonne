---

# Fiche de révision – Python

---

## 1. Introduction

* Langage interprété, simple, multi-paradigme (procédural, OO, fonctionnel).
* Exécution :

```bash
python3 script.py
```

* **Mode interactif** :

```bash
python3
```

---

## 2. Structure minimale

```python
print("Hello World")
```

Pas besoin de `;` ni de déclarer le type.

---

## 3. Variables & types

```python
age = 20           # int
pi = 3.14          # float
nom = "Adrien"     # str
vivant = True      # bool
```

Conversion :

```python
x = int("42")      # string → int
y = float("3.14")  # string → float
```

---

## 4. Entrées / sorties

```python
nom = input("Ton nom ? ")
print("Bonjour", nom)
```

---

## 5. Opérateurs

* Arithmétiques : `+ - * / // % **`
* Comparaison : `== != < > <= >=`
* Logiques : `and or not`

```python
a, b = 10, 3
print(a+b)    # 13
print(a//b)   # 3 (division entière)
print(a**b)   # 1000
print(a > b)  # True
```

---

## 6. Conditions

```python
age = 18
if age >= 18:
    print("Majeur")
elif age >= 13:
    print("Adolescent")
else:
    print("Enfant")
```

---

## 7. Boucles

```python
# For
for i in range(5):
    print("i =", i)

# While
n = 0
while n < 3:
    print(n)
    n += 1
```

`range(5)` = 0,1,2,3,4 ; `range(2,6)` = 2,3,4,5

---

## 8. Fonctions

```python
def carre(n):
    return n * n

print(carre(4))  # 16
```

Valeurs par défaut :

```python
def bonjour(nom="Inconnu"):
    print("Salut", nom)

bonjour("Adrien")
bonjour()
```

---

## 9. Collections

### Listes

```python
fruits = ["pomme", "banane", "orange"]
fruits.append("kiwi")
print(fruits[0])     # pomme
print(fruits[-1])    # kiwi
```

### Tuples (immuables)

```python
coord = (10, 20)
print(coord[0])      # 10
```

### Sets (ensembles)

```python
s = {1,2,2,3}
print(s)   # {1,2,3}
```

### Dictionnaires

```python
ages = {"Adrien": 25, "Marie": 30}
print(ages["Adrien"])   # 25
```

---

## 10. Chaînes de caractères

```python
mot = "Bonjour"
print(len(mot))         # 7
print(mot.upper())      # BONJOUR
print(mot[0:3])         # Bon
print("jour" in mot)    # True
```

---

## 11. POO – Classes & objets

```python
class Voiture:
    def __init__(self, marque, vitesse):
        self.marque = marque
        self.vitesse = vitesse

    def accelerer(self):
        self.vitesse += 10

    def afficher(self):
        print(self.marque, ":", self.vitesse, "km/h")

v1 = Voiture("BMW", 120)
v1.accelerer()
v1.afficher()   # BMW : 130 km/h
```

---

## 12. Héritage

```python
class Animal:
    def parler(self):
        print("Je suis un animal")

class Chien(Animal):
    def parler(self):
        print("Wouf!")

c = Chien()
c.parler()  # Wouf!
```

---

## 13. Exceptions

```python
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print("Erreur :", e)
finally:
    print("Toujours exécuté")
```

---

## 14. Fichiers

```python
# Écriture
with open("test.txt", "w") as f:
    f.write("Hello fichier")

# Lecture
with open("test.txt", "r") as f:
    contenu = f.read()
    print(contenu)
```

---

## 15. Modules & import

```python
import math
print(math.sqrt(16))  # 4.0

from math import pi, sin
print(pi)
```

---

## 16. List comprehensions

```python
carrés = [x*x for x in range(5)]
print(carrés)  # [0,1,4,9,16]
```

---

## 17. Exemple complet

```python
import random

nums = [random.randint(1,10) for _ in range(5)]
nums.sort()
print(nums)
```

---
