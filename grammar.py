import random
from schelet import *


def sub(d, variabilaCurenta):                           #returneaza lista cu posibile inlocuiri ale unei variabile
    sub_posibile = []
    for functie in d.get("Substitution", []):
        if variabilaCurenta == functie[0]:
            sub_posibile.append(functie[1])
    return sub_posibile

def whatWeSubbin(pozitii):
     randomSub = random.choice(pozitii)
     return randomSub

with open("grammar.txt") as f:
        d = readFile(f)

        list = d.get("VariabilaInitiala", [])[0][0]
        string = "".join(list)

        while string.islower() == False:
            pozitii = []
            for i, s in enumerate(string):
                if s.isupper():
                    pozitii.append(i)

            pozitieRandom = whatWeSubbin(pozitii)
            variabilaDeSub = string[pozitieRandom]
            sub_posibile = sub(d, variabilaDeSub)
            theOne = whatWeSubbin(sub_posibile)
            string = string[:pozitieRandom] + theOne + string[pozitieRandom + 1:]

        print(string)

             

