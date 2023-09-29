######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Juho Rekonen
# Opiskelijanumero:441410
# Päivämäärä: 6.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T1.py

# eof
import random
import math

def valikko():
    print("Mitä haluat tehdä?")
    print("1) Laske absoluuttinen arvo")
    print("2) Laske kertoma")
    print("3) Laske potenssi")
    print("4) Laske neliöjuuri")
    print("5) Arvo satunnaisluku")
    print("0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta

def Itseisarvo(luku):
    itseisarvo = math.fabs(luku)
    return itseisarvo

def Kertoma(luku):
    kertoma = math.factorial(luku)
    return kertoma

def Potenssi(luku, potenssi):
    korotus = math.pow(luku, potenssi)
    return korotus

def Nelio(luku):
    nelio = math.sqrt(luku)
    return nelio

def Arvonta(a, b):
    satunnainen = random.randint(a, b)
    return satunnainen

def paaohjelma():
    random.seed(1)
    while True:
        valinta = valikko()

        if valinta == 1:
            luku = float(input("Minkä luvun absoluuttinen arvo selvitetään: "))
            itseisarvo = Itseisarvo(luku)
            print("Luvun absoluuttinen arvo on", round(itseisarvo, 1))

        elif valinta == 2:
            luku = int(input("Minkä luvun kertoma lasketaan: "))
            kertoma = Kertoma(luku)
            print("Luvun kertoma on", kertoma)
        
        elif valinta == 3:
            luku = int(input("Mikä luku korotetaan potenssiin: "))
            potenssi = int(input("Mitä eksponenttia käytetään: "))
            korotus = Potenssi(luku, potenssi)
            print("Luku korotettuna eksponenttiin on", round(korotus, 1))
        
        elif valinta == 4:
            luku = int(input("Mikä luvun neliöjuuri lasketaan: "))
            nelio = Nelio(luku)
            print("Luvun neliöjuuri on", round(nelio, 1))
        
        elif valinta == 5:
            print("Arvotaan satunnaisluku, anna rajat kokonaislukuina.")
            min = int(input("Anna minimi (otetaan mukaan): "))
            max = int(input("Anna maksimi (otetaan mukaan): "))
            satunnainen = Arvonta(min, max)
            print("Arvottiin satunnaisluku", satunnainen)
        
        elif valinta == 0:
            print("Lopetetaan")
            break
        
        else:
            print("Tuntematon valinta, yritä uudelleen.")
        
        print()
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()






