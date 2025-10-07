from __future__ import annotations
import os
import sys
from typing import List, Dict, Tuple

#  Utils ==
def title(s: str) -> None:
    print("\n" + "="*80)
    print(s)
    print("="*80)

def step(s: str) -> None:
    print(f"[✔] {s}")

def warn(s: str) -> None:
    print(f"[!] {s}")

def ensure_data_files() -> None:
    """Crée des petits fichiers de démonstration si absents."""
    os.makedirs("data", exist_ok=True)
    # sample.txt (reprend l'exemple du sujet)
    sample_txt = os.path.join("data", "sample.txt")
    if not os.path.exists(sample_txt):
        with open(sample_txt, "w", encoding="utf-8") as f:
            f.write("ceci est un test!\n")
            f.write("il s'agit du TP de révision\n")
    # pos_analysis.txt — format simple: `<token>\t<UPOS>` par ligne
    pos_path = os.path.join("data", "pos_analysis.txt")
    if not os.path.exists(pos_path):
        with open(pos_path, "w", encoding="utf-8") as f:
            f.write("Je\tPRON\n")
            f.write("mange\tVERB\n")
            f.write("une\tDET\n")
            f.write("pomme\tNOUN\n")
            f.write("rouge\tADJ\n")
            f.write(".\tPUNCT\n")
    # french_UD_sample.conllu — mini échantillon CoNLL‑U
    conllu_path = os.path.join("data", "french_UD_sample.conllu")
    if not os.path.exists(conllu_path):
        with open(conllu_path, "w", encoding="utf-8") as f:
            f.write("# sent_id = 1\n")
            f.write("# text = Je vais souvent au marché.\n")
            f.write("1\tJe\til\tPRON\t_\t_\t2\tnsubj\t_\t_\n")
            f.write("2\tvais\taller\tAUX\t_\tMood=Ind|Tense=Pres|VerbForm=Fin\t0\troot\t_\t_\n")
            f.write("3\tsouvent\tsouvent\tADV\t_\t_\t2\tadvmod\t_\t_\n")
            f.write("4\tau\tà\tADP\t_\t_\t5\tcase\t_\t_\n")
            f.write("5\tmarché\tmarché\tNOUN\t_\tGender=Masc|Number=Sing\t2\tobl\t_\t_\n")
            f.write("6\t.\t.\tPUNCT\t_\t_\t2\tpunct\t_\t_\n")
            f.write("\n")
            f.write("# sent_id = 2\n")
            f.write("# text = La voiture rouge est très rapide.\n")
            f.write("1\tLa\tle\tDET\t_\tDefinite=Def|Gender=Fem|Number=Sing|PronType=Art\t2\tdet\t_\t_\n")
            f.write("2\tvoiture\tvoiture\tNOUN\t_\tGender=Fem|Number=Sing\t5\tnsubj\t_\t_\n")
            f.write("3\trouge\trouge\tADJ\t_\t_\t2\tamod\t_\t_\n")
            f.write("4\test\têtre\tAUX\t_\tMood=Ind|Tense=Pres|VerbForm=Fin\t5\tcop\t_\t_\n")
            f.write("5\trapide\trapide\tADJ\t_\t_\t0\troot\t_\t_\n")
            f.write("6\t.\t.\tPUNCT\t_\t_\t5\tpunct\t_\t_\n")

#  Section: Pré‑requis / venv & numpy ==
def section_numpy_import():
    title("Import numpy")
    try:
        import numpy as np  # noqa: F401
        step("numpy importé correctement (pip install numpy si besoin).")
        return True
    except Exception as e:
        warn(f"numpy non disponible: {e}. La section 'numpy' sera sautée.")
        return False

#  Variables =
def section_variables():
    title("Variables")
    x = 10
    print("1) x=10 -> type:", type(x).__name__)
    y = 3.5
    print("2) y=3.5 -> type:", type(y).__name__)
    print("3) int(y) ->", int(y))
    nom = "Adrien"  # mettez votre prénom si besoin
    print("4) nom ->", nom)

#  Listes =
def section_listes():
    title("Iterables — listes")
    lst = list(range(1, 11))
    print("1) liste 1..10 ->", lst)
    lst.append(4)
    print("2) append(4) ->", lst)
    print("3) 2 premiers ->", lst[:2])
    # supprimer le 3e élément (index 2)
    if len(lst) >= 3:
        deleted = lst.pop(2)
        print(f"4) pop(2) supprime {deleted} ->", lst)
    # ajouter 5 en 4e position (index 3)
    lst.insert(3, 5)
    print("5) insert(3,5) ->", lst)

#  Sets
def section_sets():
    title("Iterables — sets")
    mon_set = set([1, 2, 2, 3])
    print("1) set(1,2,2,3) ->", mon_set, "(pas de doublons)")
    sans_doublon = set([1, 1, 2, 2, 3])
    print("2) sans_doublon ->", sans_doublon)
    mon_set.add(5)
    print("3) add(5) ->", mon_set)
    mon_set.discard(2)
    print("4) discard(2) ->", mon_set)
    # intersection
    a = set([1, 2, 2, 3])
    b = set([1, 1, 2, 2, 3])
    inter = a & b
    print("5) intersection ->", inter)

#  Dictionnaires
def section_dicts():
    title("Dictionnaires")
    # liste comme clé -> TypeError
    try:
        d = { tuple([1,2]): "ok" }  # une liste ne peut pas être clé; tuple oui
        _ = { [1,2]: "impossible" }  # type: ignore[list-item]
    except TypeError as e:
        print("1) Une liste en clé provoque TypeError ->", e)
    capitals = {"France": "Paris", "Italie": "Rome", "Espagne": "Madrid"}
    print("2) dico pays->capitale ->", capitals)
    print("4) pays ->", list(capitals.keys()))
    print("5) capitales ->", list(capitals.values()))
    capitals["Australie"] = "Melbourne"
    print("6) +Australie:Melbourne ->", capitals)
    capitals["Australie"] = "Canberra"
    print("7) MAJ Australie:Canberra ->", capitals)
    del capitals["Australie"]
    print("8) del Australie ->", capitals)

#  Structures de contrôle ==
def section_controles(interactive: bool):
    title("Structures de contrôle — if/else, for, while")
    print("** IndentationError : impossible à exécuter sans planter volontairement.")
    print("   Exemple (commenté) :")
    print("""
# if True:
# print('mauvaise indentation')  # <- provoquerait IndentationError
""")
    # if/elif/else
    age = 17
    if age < 12:
        print("Enfant")
    elif age <= 18:
        print("Adolescent")
    else:
        print("Adulte")
    # pair/impair
    x = 7
    print("Pair" if x % 2 == 0 else "Impair")
    # for — pairs 1..20
    pairs = [n for n in range(1,21) if n % 2 == 0]
    print("Pairs 1..20:", pairs)
    # somme 0..100
    s = 0
    for n in range(101):
        s += n
    print("Somme 0..100:", s)
    # somme des carrés 1..20
    s2 = sum(n*n for n in range(1,21))
    print("Somme carrés 1..20:", s2)
    # filtrer >10
    src = [3, 8, 12, 5, 7, 20]
    filtr = [v for v in src if v > 10]
    print(" >10 :", filtr)
    # while 1..10
    i = 1
    w = []
    while i <= 10:
        w.append(i)
        i += 1
    print("while 1..10:", w)
    # while + continue (skip *3)
    i = 1
    w2 = []
    while i <= 20:
        if i % 3 == 0:
            i += 1
            continue
        w2.append(i)
        i += 1
    print("while 1..20 skip %3:", w2)
    # while + input jusqu'à somme>100 (mode auto: valeurs simulées)
    if interactive:
        total = 0
        while total <= 100:
            try:
                val = int(input("Donne un entier: "))
            except Exception:
                print("Entrée invalide, on continue...")
                continue
            total += val
        print("Somme > 100 atteinte:", total)
    else:
        total = 0
        for val in [25, 10, 50, 20]:
            total += val
            if total > 100:
                break
        print("(auto) Somme > 100 atteinte:", total)
    # demander nombres jusqu'à 0; afficher seulement les pairs
    if interactive:
        while True:
            try:
                v = int(input("Nombre (0 pour stopper): "))
            except Exception:
                print("not int -> continue")
                continue
            if v == 0:
                break
            if v % 2 != 0:
                continue
            print("pair:", v)
    else:
        demo = [3, 4, 9, 10, 0]
        out = []
        for v in demo:
            if v == 0:
                break
            if v % 2 != 0:
                continue
            out.append(v)
        print("(auto) pairs avant 0:", out)

#  Gestion des erreurs
def section_erreurs(interactive: bool):
    title("Gestion des erreurs — try/except")
    lst = [10, 20, 30, 40, 50]
    # 1) index demandé (démonstration safe)
    def get_by_index(ix: int) -> None:
        try:
            print(f"Indice {ix} ->", lst[ix])
        except IndexError:
            print(f"Indice {ix} invalide (IndexError)")
    get_by_index(2)
    get_by_index(42)  # provoque l'exception gérée
    # 2) demander un entier avec 3 tentatives max
    if interactive:
        attempts = 3
        while attempts > 0:
            try:
                v = int(input("Donne un entier: "))
                print("OK, entier:", v)
                break
            except ValueError:
                attempts -= 1
                print("Erreur: pas un entier. Tentatives restantes:", attempts)
        else:
            print("Nombre de tentatives dépassées")
    else:
        # mode auto: simulate ["abc", "1.5", "7"]
        simulated = ["abc", "1.5", "7"]
        attempts = 3
        ok = False
        for s in simulated:
            try:
                v = int(s)
                print("(auto) OK, entier:", v)
                ok = True
                break
            except ValueError:
                attempts -= 1
                print(f"(auto) '{s}' -> ValueError. Restantes:{attempts}")
                if attempts == 0:
                    print("Nombre de tentatives dépassées")
        if ok:
            pass

#  List comprehension =
def section_list_comp():
    title("List comprehension")
    # 1) ré-écrire impression des éléments (on crée plutôt une liste des éléments à imprimer)
    lst = [2, 3, 4]
    imprime = [ix for ix in lst]  # on ne print pas dans une LC ; on renvoie les valeurs
    print("1) LC de [2,3,4] ->", imprime)
    # 2) filtrer divisibles par 3 entre 1..40
    div3 = [n for n in range(1,41) if n % 3 == 0]
    print("2) divisibles par 3 (1..40) ->", div3)

#  enumerate =
def section_enumerate():
    title("enumerate")
    fruits = ["pomme", "banane", "cerise"]
    for idx, f in enumerate(fruits):
        print(f"#{idx} : {f}")
    for idx, f in enumerate(fruits, start=2):
        print(f"#{idx} : {f}")

#  Fonctions =
def cube(n: int | float) -> float:
    return n ** 3

def puissance(base: float, exposant: float) -> float:
    return base ** exposant

def convertir_temperature(temp: float, unite: str = "C") -> float:
    if unite.upper() == "C":
        return temp * 9/5 + 32
    elif unite.upper() == "F":
        return (temp - 32) * 5/9
    else:
        raise ValueError("unite doit être 'C' ou 'F'")

def section_fonctions():
    title("Fonctions")
    print("cube(3) ->", cube(3))
    print("puissance(2, 8) ->", puissance(2, 8))
    print("C->F 0°C ->", convertir_temperature(0, "C"))
    print("F->C 212°F ->", convertir_temperature(212, "F"))

#  Fichiers =
def read_pos_nouns(path: str) -> List[str]:
    nouns = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "\t" in line:
                tok, upos = line.split("\t", 1)
            else:
                parts = line.split()
                if len(parts) != 2:
                    continue
                tok, upos = parts
            if upos.upper() == "NOUN":
                nouns.append(tok)
    return nouns

def parse_conllu(path: str) -> Tuple[int, List[str], List[str]]:
    sentences = 0
    aux, adjs = [], []
    with open(path, "r", encoding="utf-8") as f:
        in_sentence = False
        for line in f:
            line = line.rstrip("\n")
            if not line:
                if in_sentence:
                    sentences += 1
                    in_sentence = False
                continue
            if line.startswith("#"):
                in_sentence = True
                continue
            # ID FORM LEMMA UPOS ...
            cols = line.split("\t")
            if len(cols) >= 4:
                form, upos = cols[1], cols[3].upper()
                if upos == "AUX":
                    aux.append(form)
                elif upos == "ADJ":
                    adjs.append(form)
                in_sentence = True
    # dernière phrase si fichier ne se termine pas par ligne vide
    if in_sentence:
        sentences += 1
    return sentences, aux, adjs

def section_fichiers():
    title("Manipulation de fichiers")
    ensure_data_files()
    # Lire sample.txt (exemple sujet)
    with open("data/sample.txt", "r", encoding="utf-8") as f:
        content = f.read()
    print("-- data/sample.txt --\n" + content, end="")
    # Lecture ligne par ligne
    with open("data/sample.txt", "r", encoding="utf-8") as f:
        for ix, line in enumerate(f):
            print(f"LINE {ix}: {line.strip()}")
    # Ecriture output.txt
    lines = ["This is line 1", "This is line 2"]
    with open("output.txt", "w", encoding="utf-8") as f:
        for l in lines:
            f.write(l + "\n")
    step("output.txt écrit (overwrite).")
    # Exercices
    nouns = read_pos_nouns("data/pos_analysis.txt")
    print("1) NOUNs dans pos_analysis.txt ->", nouns)
    sent_n, aux, adjs = parse_conllu("data/french_UD_sample.conllu")
    print("2) nb phrases conllu ->", sent_n)
    print("   AUX ->", aux)
    print("   ADJ ->", adjs)
    # Pour aller plus loin: écrire auxiliary.txt
    with open("auxiliary.txt", "w", encoding="utf-8") as f:
        for w in aux:
            f.write(w + "\n")
    step("3) auxiliary.txt écrit.")

#  NumPy =
def section_numpy():
    title("NumPy")
    try:
        import numpy as np
    except Exception as e:
        warn(f"numpy indisponible: {e}.")
        return
    x = np.array([1, 2, 3])
    y = np.array([10, 20, 30])
    print("x+y ->", x + y)
    print("x*y ->", x * y)
    print("x**2 ->", x ** 2)
    arr = np.array([1, 2, 3, 4, 5])
    print("sum:", np.sum(arr))
    print("mean:", np.mean(arr))
    print("max:", np.max(arr))
    print("sqrt:", np.sqrt(arr))
    d = np.array([[1,2,3], [4,5,6], [7,8,9]])
    print("row means:", d.mean(axis=1))
    # Exercices
    # 1) cube des éléments [2,3,4] sans for
    a = np.array([2,3,4]) ** 3
    print("1) cubes [2,3,4] ->", a)
    # 2) éléments > moyenne
    arr2 = np.array([1, 10, 5, 7, 2, 9])
    mean2 = arr2.mean()
    print("2) >", mean2, "->", arr2[arr2 > mean2])
    # 3) somme par ligne
    print("3) row sums:", d.sum(axis=1))
    # 4) tableau aléatoire
    rng = np.random.default_rng(42)
    rnd = rng.integers(low=0, high=100, size=(3,5))
    print("4) random 3x5:\n", rnd)
    # 5) nombre d'éléments pairs
    print("5) nb pairs:", int((rnd % 2 == 0).sum()))

#  Pour aller plus loin =
def somme_indices_pairs(liste: List[int | float]) -> float:
    return sum(v for i, v in enumerate(liste) if i % 2 == 0)

def trouver_doublons(liste: List[object]) -> List[object]:
    seen = set()
    dups = set()
    for x in liste:
        if x in seen:
            dups.add(x)
        else:
            seen.add(x)
    return sorted(dups, key=lambda z: str(z))

def mot_plus_long(phrases: List[str]) -> Tuple[str, str]:
    best_word = ""
    best_sent = ""
    for s in phrases:
        for w in s.split():
            if len(w) > len(best_word):
                best_word, best_sent = w, s
    return best_word, best_sent

def frequence_lettres(texte: str) -> Dict[str, int]:
    freq: Dict[str, int] = {}
    for ch in texte.lower():
        if "a" <= ch <= "z":
            freq[ch] = freq.get(ch, 0) + 1
    return freq

def section_problemes():
    title("Pour aller plus loin — problèmes")
    print("1) somme_indices_pairs([10,20,30,40,50]) ->", somme_indices_pairs([10,20,30,40,50]))
    print("2) trouver_doublons([1,2,3,2,4,1,5]) ->", trouver_doublons([1,2,3,2,4,1,5]))
    phrases = ["Bonjour à tous", "Python est fantastique", "J'aime coder"]
    print("3) mot_plus_long ->", mot_plus_long(phrases))
    print("4) frequence_lettres('Bonjour Python !') ->", frequence_lettres("Bonjour Python !"))

#  main ==
def main():
    interactive = ("--interactive" in sys.argv)
    ensure_data_files()
    has_numpy = section_numpy_import()
    section_variables()
    section_listes()
    section_sets()
    section_dicts()
    section_controles(interactive=interactive)
    section_erreurs(interactive=interactive)
    section_list_comp()
    section_enumerate()
    section_fonctions()
    section_fichiers()
    if has_numpy:
        section_numpy()
    section_problemes()
    print("\nFin. Tout est OK.\n")

if __name__ == "__main__":
    main()
