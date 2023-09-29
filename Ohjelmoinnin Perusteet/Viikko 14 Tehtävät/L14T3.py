######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Juho Rekonen
# Opiskelijanumero:441410
# Päivämäärä: 12.12.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L14T3.py

# eof

import datetime

def paaohjelma():
    # Kysytään käyttäjältä vuosi ja kuukausi
    vuosi = int(input("Anna vuosi: "))
    kuukausi = int(input("Anna kuukausi: "))
    print("Kalenteri näyttää seuraavalle:")

    # Muodostetaan ensimmäinen päivä, jotta tiedetään, mistä viikonpäivästä kuukausi alkaa.
    ekapaiva = datetime.date(vuosi, kuukausi, 1)
    
    # Lasketaan montako päivää kuukaudessa on
    vikapaiva = ekapaiva + datetime.timedelta(days=32)
    paivat = vikapaiva.replace(day=1) - datetime.timedelta(days=1)

    viikonpaivat = ["Ma", "Ti", "Ke", "To", "Pe", "La", "Su"]
    for paiva in viikonpaivat:
        print("{:>3}".format(paiva), end="")
    print()

    # Tulostetaan ensimmäisen rivin tyhjät välit, jos kuukausi ei ala maanantaista
    for i in range(ekapaiva.weekday()):
        print("{:>3}".format(""), sep="", end="")

    # Print the days of the month
    for i in range(1, paivat.day + 1):
        print("{:>3}".format(i), sep="", end="")
        # If this is the last day of the week, start a new line
        if (ekapaiva.weekday() + i) % 7 == 0:
            print()
    
    return None

paaohjelma()


