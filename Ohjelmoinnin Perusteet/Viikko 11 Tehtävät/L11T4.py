######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Juho Rekonen
# Opiskelijanumero:441410
# Päivämäärä: 21.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L11T4.py

# eof

import time
import sys

class TULOKSET:
    Suurempi = None
    Pienempi = None

def hakufunktio(Nimi, Luvut):
    try:
        lista = [] # Lisätään tiedoston luvut kokonaislukuina listaan
        luenta = open(Nimi, "r")
        koko = luenta.readlines()
        for i in range(0, len(koko)):
            lista.append(int(koko[i].replace("\n", "")))
        # Käydään listan alkioita yksitellen läpi vertaillen sitä kaikkiin muihin alkioihin 
        vastaus = False
        for alkio in lista:
            b = lista[0]
            for i in range(1, len(lista)):
                # Testataan, jos suurempi luku on pienemmän oikealla puolella
                if alkio * 3 < b:
                    vastaus = True
                    Luvut.Suurempi = b
                    Luvut.Pienempi = alkio
                    break
                # Suurempi luku on pienemmän vasemmalla puolella
                elif b * 3 < alkio:
                    vastaus = True
                    Luvut.Suurempi = alkio
                    Luvut.Pienempi = b
                    break
                else:
                    b = lista[i]
            # Vastaus saa arvon True, jolloin hypätään ulos ulommasta loopista
            if vastaus == True:
                break

    except Exception:
        print("Tiedoston", ("'" + Nimi + "'") , "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

    return Luvut

def paaohjelma():
    Nimi = input("Anna luettavan tiedoston nimi: ")
    Tulokset = TULOKSET()
    Aloitus = time.perf_counter()
    Tulokset = hakufunktio(Nimi, Tulokset)
    Lopetus = time.perf_counter()
    Aika = Lopetus - Aloitus

    if ((Tulokset.Suurempi == None) and (Tulokset.Pienempi == None)):
        print("Hakualgoritmi ei löytänyt sopivaa lukuparia.")
    elif (Aika > 2):
        print("Hakualgoritmi ei ollut tarpeeksi nopea.")
    else:
        print("Hakualgoritmi oli riittävän nopea!")
        print("Se löysi sopivan parin:", Tulokset.Pienempi, "ja", Tulokset.Suurempi)

    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

