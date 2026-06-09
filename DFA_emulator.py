import sys
from schelet import *

def delta(d, stareCurenta, caracter):
    for functie in d.get("Delta", []):
        if stareCurenta == functie[0] and caracter == functie[1]:
            return functie[2]
    return None
            
def validare(d, string):
    stareCurenta = d.get("StareInitiala", [])[0][0]
    for c in string:
        if c not in d.get("Sigma", [])[0]:
            print("Cuvantul contine caractere din afara alfabetului. Incearca din nou!")
            validare(d)
        else:
            stareCurenta = delta(d, stareCurenta, c)

    if stareCurenta in d.get("StareFinala", [])[0]:
        print("Cuvant acceptat!")
    else:
        print("Cuvantul nu este acceptat")

def finalizare(fisier, string):
    with open(fisier) as f:
        d = readFile(f)
        validare(d, string)

if len(sys.argv) != 2:
    print("Utilizare: python3 DFA_emulator.py <cuvant>")
else:
    cuvant = sys.argv[1]
    finalizare("DFA_script.txt", cuvant)