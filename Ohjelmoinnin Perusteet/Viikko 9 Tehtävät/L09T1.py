import sys

def tiedostoLue(lista, tiedosto):
    try:
        luenta = open(tiedosto, "r")
        koko = luenta.readlines()
        for i in range(0, len(koko)):
            rivi = koko[i].strip()
            lista.append(rivi)
        luenta.close()
        return lista
    except Exception:
        print("Tiedoston", ("'" + tiedosto + "'"), "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return None

def tiedostoKirjoita(lista, tiedosto):
    try:
        kirjoitus = open(tiedosto, "w")
        for luku in lista:
            kirjoitus.write(str(luku) + "\n")
        kirjoitus.close()
        return None
    except Exception:
        print("Tiedoston", ("'" + tiedosto + "'"), "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return None

def paaohjelma():
    lista = []
    luenta = input("Anna luettavan tiedoston nimi: ")
    lista = tiedostoLue(lista, luenta)
    print("Tiedoston", ("'" + luenta + "'"), "lukeminen onnistui,", len(lista), "riviä.")
    kirjoitus = input("Anna kirjoitettavan tiedoston nimi: ")
    tiedostoKirjoita(lista, kirjoitus)
    print("Tiedoston", ("'" + kirjoitus + "'"), "kirjoittaminen onnistui.")
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
    
