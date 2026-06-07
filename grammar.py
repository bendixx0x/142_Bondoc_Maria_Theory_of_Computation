"""
funtii:
-verificare cate variabile ai in string si returnarea pozitiei lor si daca nu e niciun return la cuvant
-alegerea variabilelor care se vor substitui random
-alegerea random a unei substitutii din lista
-inlocuirea in string cu sub-ul
"""
import random
from schelet import *


def sub(d, variabilaCurenta):
    variabile_posibile = []
    for functie in d.get("Substitution", []):
        if variabilaCurenta == functie[0]:
            variabile_posibile.append(functie[1])
    return variabile_posibile

def whatWeSubbin(d):
     random = random.randrange(0, len(d)-1)
     return random

with open("grammar.txt") as f:
        d = readFile(f)

        string = d.get("VariabilaInitiala", [])[0]


        ok = 1
        visited = {}
        i = 0
        for s in string:
            i += 1
            if s.isupper() and s not in visited:
                visited[s] = i
                ok = 0
            elif s in visited:
                visited[s].append(i)
        if ok == 1:
            print(string)
            f.close()

        pozitieRandom = whatWeSubbin(visited)
        theSub = [v for v, poz in visited if poz == pozitieRandom]
        len = len(visited[theSub])
        if len != 1:
            len = random.randrange(0, len-1)

             

