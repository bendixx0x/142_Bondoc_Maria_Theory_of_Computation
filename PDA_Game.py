from schelet import *

def delta(d, stareCurenta, caracter):
    stari_posibile = []
    for functie in d.get("Delta", []):
        if stareCurenta == functie[0] and caracter == functie[1]:
            stari_posibile.append(functie[2])
    return stari_posibile

def getStariSpeciale(d):
    speciale = {}
    for entry in d.get("StareSpeciala", []):
        camera, item = entry[0], entry[1]
        speciale[camera] = item
    return speciale

def validare(d):
    string = input("Introdu drumul pe care vrei sa il urmezi:").strip()
    pasi = [p.strip() for p in string.split(",")] if string else []

    stariSpeciale = getStariSpeciale(d)
    sigma = d.get("Sigma", [])[0]
    stariFinale = set(d.get("StareFinala", [])[0])
    stareInitiala = d.get("StareInitiala", [])[0][0]
    
   
    configuratii = [(stareInitiala, ['$'], set())]

    # Verificam starea initiala: are cheie?
    configuratii = _colecteazaChei(configuratii, stareInitiala, stariSpeciale)

    for pas in pasi:
        if pas not in sigma:
            print(f"Directia '{pas}' nu face parte din alfabet {sigma}. Incearca din nou!")
            validare(d)
            return

        configuratiiNoi = []
        for (stare, stiva, vizitate) in configuratii:
            stariUrmatoare = delta(d, stare, pas)
            for stareNoua in stariUrmatoare:
                stivaNou = list(stiva)
                vizitateNoi = set(vizitate)

                # Daca starea noua are cheie si n-am luat-o inca
                if stareNoua in stariSpeciale and stareNoua not in vizitateNoi:
                    stivaNou.append(stariSpeciale[stareNoua])  # punem cheia pe stiva
                    vizitateNoi.add(stareNoua)

                configuratiiNoi.append((stareNoua, stivaNou, vizitateNoi))

        configuratii = configuratiiNoi

        if not configuratii:
            print("Nu exista nicio cale valida. Drum blocat!")
            return

    # Verificam conditiile de acceptare
    numarCheiNecesare = len(stariSpeciale)  # 2 in cazul tau
    
    for (stare, stiva, vizitate) in configuratii:
        cheiPeStiva = [x for x in stiva if x != '$']
        if stare in stariFinale and len(cheiPeStiva) >= numarCheiNecesare:
            print(f"Drum acceptat! Ai ajuns in '{stare}' cu {len(cheiPeStiva)} chei: {cheiPeStiva}")
            return

    # Afisam de ce a esuat
    for (stare, stiva, vizitate) in configuratii:
        cheiPeStiva = [x for x in stiva if x != '$']
        if stare in stariFinale:
            print(f"Ai ajuns in '{stare}', dar ai doar {len(cheiPeStiva)}/{numarCheiNecesare} chei. Incearca un alt drum!")
            return
    
    print(f"Drum respins. Nu ai ajuns in starea finala {stariFinale}.")

def _colecteazaChei(configuratii, stareInitiala, stariSpeciale):
    """Verifica daca starea initiala are deja o cheie."""
    rezultat = []
    for (stare, stiva, vizitate) in configuratii:
        stivaNou = list(stiva)
        vizitateNoi = set(vizitate)
        if stare in stariSpeciale and stare not in vizitateNoi:
            stivaNou.append(stariSpeciale[stare])
            vizitateNoi.add(stare)
        rezultat.append((stare, stivaNou, vizitateNoi))
    return rezultat

def finalizare(fisier):
    with open(fisier) as f:
        d = readFile(f)
        validare(d)

finalizare("Game.txt")