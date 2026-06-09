import sys
from schelet import *


def delta(d, stareCurenta, caracter):
    stari_posibile = []

    for functie in d.get("Delta", []):
        if stareCurenta == functie[0] and caracter == functie[1]:
            stari_posibile.append(functie[2])

    return stari_posibile


def epsiClosure(d, stari):
    closure = set(stari)
    stiva = list(stari)

    while stiva:
        stare = stiva.pop()

        for stareNoua in delta(d, stare, "epsi"):
            if stareNoua not in closure:
                closure.add(stareNoua)
                stiva.append(stareNoua)

    return closure


def validare(d, string):
    stareInitiala = d.get("StareInitiala", [])[0][0]
    stariCurente = epsiClosure(d, {stareInitiala})

    for c in string:
        if c not in d.get("Sigma", [])[0]:
            print(
                "Cuvantul contine caractere din afara alfabetului."
            )
            return

        stariNoi = set()

        for stare in stariCurente:
            for stareNoua in delta(d, stare, c):
                stariNoi.add(stareNoua)

        stariCurente = epsiClosure(d, stariNoi)

    stariFinale = set(d.get("StareFinala", [])[0])

    if stariCurente & stariFinale:
        print("Cuvantul este acceptat!")
    else:
        print("Cuvantul nu este acceptat.")


def finalizare(fisier, string):
    with open(fisier) as f:
        d = readFile(f)
        validare(d, string)


if len(sys.argv) != 2:
    print("Utilizare: python3 NFA_emulator.py <cuvant>")
else:
    cuvant = sys.argv[1]
    finalizare("NFA_script.txt", cuvant)