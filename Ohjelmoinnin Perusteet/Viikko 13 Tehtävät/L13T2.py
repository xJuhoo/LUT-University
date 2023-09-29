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
# Tehtävä L13T2.py

# eof

import sys

def paaohjelma():
    luvut = []
    for parametri in sys.argv[1:]:
        try:
            if int(parametri) % 2 == 0:
                luvut.append(int(parametri))
            else:
                continue

        except ValueError:
            pass

    print("Syötteen parilliset luvut ovat seuraavat:")
    for luku in luvut:
        print("{} ".format(luku), end="")

    print()
    try:
        keskiarvo = round(sum(luvut) / len(luvut), 2)
        print("Lukujen keskiarvo on {0:.2f}.".format(keskiarvo))
    except ZeroDivisionError:
        print("Nollalla jako, anna parametreiksi kokonaislukuja.")
    print("Kiitos ohjelman käytöstä.")
    luvut.clear()
    return None

paaohjelma()

