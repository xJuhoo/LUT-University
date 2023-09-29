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
# Tehtävä L14T4.py

# eof

import sys
import random

# Aliohjelma lukujen valitsemiseen väliltä [a, b].
def arvoLuvut(lukumaara, a, b, lista):
  # Tarkistetaan, että yläraja on suurempi kuin alaraja
    if b <= a:
        print("Ylärajan tulee olla suurempi kuin alarajan.")

  # Tarkistetaan, että annetulta väliltä voi valita annetun määrän lukuja
    elif lukumaara > b - a + 1:
        print("Annetulta väliltä ei voi valita annettua määrää lukuja.")
    
    else:
        # Arvotaan numerot ja palautetaan ne listana
        for _ in range(lukumaara):
            luku = random.randint(a, b)
           # Tarkistetaan, onko arvottu numero lisätty jo listaan
            while luku in lista:
            # Jos on, arvotaan uusi luku
                luku = random.randint(a, b)
            lista.append(luku)

    return lista

# Aliohjelma lukujen kirjoittamiselle
def kirjoitaTiedosto(tiedosto, lukumaara, a, b, lista):
    try:
        open(tiedosto, "w", encoding="utf-8").close()
        kirjoitus = open(tiedosto, "a", encoding="utf-8")
        kirjoitus.write("Arvottu {} lukua väliltä {}-{}:\n".format(lukumaara, a, b))
        for luku in lista:
            kirjoitus.write("{}\n".format(luku))
        kirjoitus.close()
        print("Tiedosto '{}' luotu, kiitos ohjelman käytöstä.".format(tiedosto))
    except Exception:
        print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.".format(tiedosto))
        sys.exit(0)
    return None

def paaohjelma():
    Luvut = []
    random.seed(1)
    print("Tämä ohjelma arpoo haluamasi määrän kokonaislukuja halutulta väliltä")
    print("ja kirjoittaa ne tekstitiedostoon.")
    tiedosto = input("Anna tehtävän tiedoston nimi: ")
    valinnat = input("Anna lukujen määrä, alaraja ja yläraja, esim. 7 1 37: ").split(" ")
    lukumaara = int(valinnat[0])
    alaraja = int(valinnat[1])
    ylaraja = int(valinnat[2])
    Luvut = arvoLuvut(lukumaara, alaraja, ylaraja, Luvut)
    kirjoitaTiedosto(tiedosto, lukumaara, alaraja, ylaraja, Luvut)
    Luvut.clear()
    
    return None

paaohjelma()


