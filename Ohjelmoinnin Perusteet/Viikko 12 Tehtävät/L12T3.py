######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Juho Rekonen
# Opiskelijanumero:441410
# Päivämäärä: 28.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L12T3.py

# eof

import jsonpickle
import sys

class TIEDOT:
    Nimike = None
    Tekija = None
    ISBN = None
    Varauksia = None
    Niteita = None
    Lisakappaleita = None
    VarauksiaPerNide = None

# Valikkopohjainen ohjelma
def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue CSV tiedosto")
    print("2) Lue JSON tiedosto")
    print("3) Kirjoita CSV tiedosto")
    print("4) Kirjoita JSON tiedosto")
    print("0) Lopeta")

    # Tarkistetaan käyttäjän antama syöte merkkijonojen varalta
    while True:
        try:
            valinta = int(input("Anna valintasi: "))
        except ValueError:
            print("Anna valinta kokonaislukuna.")
        else:
            break
    return valinta

# Aliohjelma tiedoston kysymiselle
def kysyTiedosto(kehote):
    tiedosto = input("Anna " + kehote + " tiedoston nimi: ")
    return tiedosto

# Aliohjelma CSV tiedoston lukemiselle
def lueCSV(tiedosto, lista):
    try:
        luenta = open(tiedosto, "r", encoding="utf-8")
        koko = luenta.readlines()
        for i in range(1, len(koko)):
            Kirja = TIEDOT() # Luodaan kirjoista omat oliot
            rivi = koko[i].replace("\n", "").split(";")
            Kirja.Nimike = rivi[0]
            Kirja.Tekija = rivi[1]
            Kirja.ISBN = rivi[2]
            Kirja.Varauksia = int(rivi[3])
            Kirja.Niteita = int(rivi[4])
            Kirja.Lisakappaleita = int(rivi[5])
            Kirja.VarauksiaPerNide = float(rivi[6])
            lista.append(Kirja)
        luenta.close()
    except Exception:
        print("Tiedoston", ("'" + tiedosto + "'"), "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print("Luettu", len(lista), "kirjan tiedot.")
    return lista

def lueJSON(tiedosto, lista):
    try:
        luenta = open(tiedosto, "r", encoding="utf-8")
        lista = jsonpickle.decode(luenta.read())
        luenta.close()
    except Exception:
        print("Tiedoston", ("'" + tiedosto + "'"), "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print("Luettu", len(lista), "kirjan tiedot.")
    return lista

def kirjoitaCSV(tiedosto, lista):
    try:
        open(tiedosto, "w").close()
        kirjoitus = open(tiedosto, "a", encoding="utf-8")
        kirjoitus.write("Nimike;Tekijä;ISBN;Varauksia;Niteitä;Tilattuja lisäkappaleita;Varauksia / nide\n")
        for kirja in lista:
            kirjoitus.write(kirja.Nimike + ";" + kirja.Tekija + ";" + kirja.ISBN + ";" + str(kirja.Varauksia) + ";")
            kirjoitus.write(str(kirja.Niteita) + ";" + str(kirja.Lisakappaleita) + ";" + str(kirja.VarauksiaPerNide) + "\n")
        kirjoitus.close()
    except Exception:
        print("Tiedoston", ("'" + tiedosto + "'"), "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print("Tiedosto", tiedosto, "kirjoitettu.")
    return None

def kirjoitaJSON(tiedosto, lista):
    try:
        open(tiedosto, "w").close()
        kirjoitus = open(tiedosto, "a", encoding="utf-8")
        kirjoitus.write(jsonpickle.encode(lista, indent=4))
        kirjoitus.close()
    except Exception:
        print("Tiedoston", ("'" + tiedosto + "'"), "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print("Tiedosto", tiedosto, "kirjoitettu.")
    return None

# Pääohjelma
def paaohjelma():
    Kirjat = [] # Lista, johon tallennetaan kirja-oliot

    while True:
        valinta = valikko()

        if valinta == 1:
            Kirjat.clear
            luenta = kysyTiedosto("luettavan CSV")
            Kirjat = lueCSV(luenta, Kirjat)
        
        elif valinta == 2:
            Kirjat.clear
            luenta2 = kysyTiedosto("luettavan JSON")
            Kirjat = lueJSON(luenta2, Kirjat)
        
        elif valinta == 3:
            kirjoitus = kysyTiedosto("kirjoitettavan CSV")
            kirjoitaCSV(kirjoitus, Kirjat)

        elif valinta == 4:
            kirjoitus2 = kysyTiedosto("kirjoitettavan JSON")
            kirjoitaJSON(kirjoitus2, Kirjat)
        
        elif valinta == 0:
            Kirjat.clear()
            break
        
        else:
            print("Tuntematon valinta, yritä uudelleen.")
        print()
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

