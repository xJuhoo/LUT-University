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
# Tehtävä L08T2.py

# eof

import L08T2Kirjasto

def valikko():
    print("Minkä muunnoksen haluat tehdä?")
    print("1) Anna muunnettava tilavuus")
    print("2) Muunna litra gallon'ksi")
    print("3) Muunna litra pint'ksi")
    print("4) Muunna litra cup'ksi")
    print("5) Muunna litra fluid ounce'ksi")
    print("6) Muunna gallon litroiksi")
    print("7) Muunna pint litroiksi")
    print("8) Muunna cup litroiksi")
    print("9) Muunna fluid ounce litroiksi")
    print("0) Lopeta")

    valinta = int(input("Anna valintasi: "))
    return valinta

def paaohjelma():
    print("Käytetään kirjaston versiota", L08T2Kirjasto.versio)

    while True:
        valinta = valikko()

        if valinta == 1:
            tilavuus = float(input("Anna muunnettava tilavuus desimaalilukuna: "))
        
        elif valinta == 2:
            muunnos = L08T2Kirjasto.litraG(tilavuus)
            print("Litrat muutettuina gallon'ksi:", round(muunnos, 2))
        
        elif valinta == 3:
            muunnos = L08T2Kirjasto.litraP(tilavuus)
            print("Litrat muutettuina pint'ksi:", round(muunnos, 2))
        
        elif valinta == 4:
            muunnos = L08T2Kirjasto.litraC(tilavuus)
            print("Litrat muutettuina cup'ksi:", round(muunnos, 2))
        
        elif valinta == 5:
            muunnos = L08T2Kirjasto.litraFO(tilavuus)
            print("Litrat muutettuina fluid ounce'ksi:", round(muunnos, 2))
        
        elif valinta == 6:
            muunnos = L08T2Kirjasto.GallonL(tilavuus)
            print("Gallon't muutettuina litroiksi:", round(muunnos, 2))
        
        elif valinta == 7:
            muunnos = L08T2Kirjasto.PintL(tilavuus)
            print("Pint't muutettuina litroiksi:", round(muunnos, 2))
        
        elif valinta == 8:
            muunnos = L08T2Kirjasto.CupL(tilavuus)
            print("Cup't muutettuina litroiksi:", round(muunnos, 2))
        
        elif valinta == 9:
            muunnos = L08T2Kirjasto.FluidOunceL(tilavuus)
            print("Fluid ounce't muutettuina litroiksi:", round(muunnos, 2))
        
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
