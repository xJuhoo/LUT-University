######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Juho Rekonen
# Opiskelijanumero: 441410
# Päivämäärä: 21.10.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L07T4.py

# eof

class TULOS:
    Pienin = 0
    Suurin = 0
    Summa = 0
    Keskiarvo = 0


def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Anna tiedostonimet")
    print("2) Lue tiedosto")
    print("3) Analysoi")
    print("4) Kirjoita tiedosto")
    print("0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta

def kysyTiedosto(nykyinen, kehote):
    print(kehote, "tiedoston nimi on", nykyinen + ".")
    uusi = input("Anna uusi nimi, enter säilyttää nykyisen: ")
    if not uusi:
        return nykyinen
    else :
        return uusi
    
def lueTiedosto(tiedosto):
    lista = []
    luenta = open(tiedosto, "r")
    koko = luenta.readlines()
    for i in range(0, len(koko)):
        rivi = koko[i].replace("\n", "")
        lista.append(rivi)
    return lista

def laskeArvot(lista, tiedot):
    tietolista = []
    arvot = {int(i) for i in lista}
    tiedot.Pienin = min(arvot)
    tiedot.Suurin = max(arvot)
    tiedot.Summa = sum(arvot)
    tiedot.Keskiarvo = round(sum(arvot) / len(lista), 0)
    tietolista.append(tiedot)
    return tietolista
    
def tulostaTiedot(analyysi, tiedosto):
    kirjoitus = open(tiedosto, "w")
    for tiedot in analyysi:
        kirjoitus.write("Analyysin tulokset ovat seuraavat:" + "\n")
        kirjoitus.write("Datan pienin arvo on " + str(tiedot.Pienin) + "." + "\n")
        kirjoitus.write("Datan suurin arvo on " + str(tiedot.Suurin) + "." + "\n")
        kirjoitus.write("Datan summa on " + str(tiedot.Summa) + "." + "\n")
        kirjoitus.write("Datan keskiarvo on " + str(tiedot.Keskiarvo) + "." + "\n")
    kirjoitus.close()
    return None

    
def paaohjelma():
    tiedot = TULOS()
    nykyinen = "''"
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    
    while True:
        valinta = valikko()
        if (valinta == 1):
            print("Anna tiedostonimet")
            luenta = kysyTiedosto(nykyinen, "Luettavan")
            kirjoitus = kysyTiedosto(nykyinen, "Kirjoitettavan")
        elif (valinta == 2):
            lista = lueTiedosto(luenta)
            print("Tiedosto", ("'" + luenta + "'"), "luettu.")
        elif (valinta == 3):
            analyysi = laskeArvot(lista, tiedot)
            print("Analyysi suoritettu.")
        elif (valinta == 4):
            tulostaTiedot(analyysi, kirjoitus)
            print("Tulokset kirjoitettu tiedostoon.")
        elif (valinta == 0):
            print("Lopetetaan")
            break
        else :
            print("Tuntematon valinta, yritä uudestaan.")
        print()
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
