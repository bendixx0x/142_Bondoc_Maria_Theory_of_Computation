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

def validare(d):
    string = input("Introdu cuvantul pe care vrei sa il verifici: ")
    
    stareInitiala = d.get("StareInitiala", [])[0][0]
    stariCurente = epsiClosure(d, {stareInitiala})

    for c in string:
        if c not in d.get("Sigma", [])[0]:
            print("Cuvantul contine caractere din afara alfabetului. Incearca din nou!")
            validare(d)
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

def finalizare(fisier):
    with open(fisier) as f:
        d = readFile(f)
        validare(d)

finalizare("NFA_script.txt")


#fara input -> ar fi mai bine sa fie in command line