######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Juho Rekonen
# Opiskelijanumero:441410
# Päivämäärä: 6.12.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L13T1Kirjasto.py

# eof

import sys

class HENKILO:
    Nimi = None
    Ika = None
    Puh = None

def kysyTiedosto(kehote):
    tiedosto = input("Anna {} tiedoston nimi: ".format(kehote))
    return tiedosto

def analysoiTiedot(tiedosto, lista):
    try:
        luenta = open(tiedosto, "r", encoding="utf-8")
        koko = luenta.readlines()
        for i in range(0, len(koko)):
            Henkilo = HENKILO()
            rivi = koko[i].replace("\n", "").split(";")
            Henkilo.Nimi = rivi[0]
            Henkilo.Ika = int(rivi[2])
            Henkilo.Puh = rivi[1]
            lista.append(Henkilo)
        luenta.close()
    except Exception:
        print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.".format(tiedosto))
        sys.exit(0)
    return lista

def tulostaTiedot(lista):
    for henkilo in lista:
        print("{} on {} vuotta vanha ja hänen puhelinnumero on {}.".format(henkilo.Nimi, henkilo.Ika, henkilo.Puh))
    return None

def kysyLuku():
    while True:
        try:
            luku = int(input("Minkä ikäiset ihmiset otetaan mukaan tiedostoon (vuosia): ").strip())
        except ValueError:
            print("Anna vuosiluku kokonaislukuna.")
        else:
            break
    return luku

def kirjoitaTiedot(lista):
    valitut = []
    summa = 0
    vuosi = kysyLuku()
    try:
        open("tulos.txt", "w").close()
        for henkilo in lista:
            if henkilo.Ika >= vuosi:
                valitut.append(henkilo)
                summa += 1
            else:
                continue
        
        kirjoitus = open("tulos.txt", "a", encoding="utf-8")
        kirjoitus.write("Tiedostossa on mukana {} vähintään {} vuotiasta henkilöä:\n".format(summa, vuosi))
        for henkilo in valitut:
            kirjoitus.write("{};{};{}\n".format(henkilo.Nimi, henkilo.Puh, henkilo.Ika))
        kirjoitus.close()
    except Exception:
        print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.".format("tulos.txt"))
        sys.exit(0)
    valitut.clear()
    return None