######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Juho Rekonen
# Opiskelijanumero:441410
# Päivämäärä: 15.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L10T3.py

# eof

import numpy

def paaohjelma():
    print("Tämä ohjelma testaa numpy-matriisin käyttöä.")
    # Merkitään matematiikasta tutulla tyylillä matriisia isolla kirjaimella
    A = numpy.zeros((4, 4), int)
    for rivi in range(4):
        for sarake in range(4):
            A[rivi][sarake] = (rivi + 1) * (sarake + 1)

    print("Matriisi tulostettuna numpy-muotoilulla:")
    print(A)
    print()
    print("Matriisi tulostettuna alkiot puolipisteillä eroteltuna:")
    for rivi in range(4):
        for sarake in range(4):
            print(A[rivi][sarake], end = ";")
        print()
    print()
    A = numpy.delete(A, numpy.s_[:], None)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

