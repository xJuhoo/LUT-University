######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Juho Rekonen
# Opiskelijanumero:441410
# Päivämäärä: 9.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L09T3.py

# eof

import sys
class AUTO:
    merkki = None

def lueTiedosto(tiedosto, lista):
    try:
        luenta = open(tiedosto, "r")
        koko = luenta.readlines()
        for i in range(0, len(koko)): # Näin saadaan lopetettua ennen viimeistä tyhjää riviä
            rivi = koko[i].strip() # Poistetaan rivinvaihtomerkki rivin lopusta.
            lista.append(rivi)
        luenta.close()
    except Exception:
        print("Tiedoston", ("'" + tiedosto + "'"), "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

    return lista

def analysoiTiedosto(lista):
    automerkit = []
    lkm = 0 # Lasketaan eri automerkkien määrät
    tarkistus = lista[0] # Tarkistetaan, onko automerkki vaihtunut
    for autot in lista:
        auto = AUTO()
    # Tutkitaan jos automerkki vaihtuu
        if tarkistus != autot:
            auto.merkki = tarkistus
            tarkistus = autot
            lkm += 1
            automerkit.append(auto)
    # Tutkitaan jos tiedosto loppuu eli päästään viimeiseen alkioon
        elif tarkistus == autot and autot == lista[-1]:
            auto.merkki = tarkistus
            automerkit.append(auto)
            lkm += 1
            break
    # Muissa tapauksissa tarkistus ja automerkki ovat samoja
        elif tarkistus == autot:
            continue
    
    return [automerkit, lkm]

def tallennaTiedosto(tiedosto, lista, arvo):
    try:
        open(tiedosto, "w").close()
        kirjoitus = open(tiedosto, "a", encoding = "utf-8")
        for automerkki in lista:
            kirjoitus.write(automerkki.merkki + "\n")
        kirjoitus.close()
    except Exception:
        print("Tiedoston", ("'" + tiedosto + "'"), "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    # Kirjoitetaan tiedot vielä käyttäjälle
    print("Tiedostossa oli", str(arvo), "eri automerkkiä.")
    for automerkki in lista:
        print(automerkki.merkki)
    
    return None


def paaohjelma():
    lista = []
    automerkit = []
    luenta = input("Anna luettavan tiedoston nimi: ")
    kirjoitus = input("Anna kirjoitettavan tiedoston nimi: ")
    lista = lueTiedosto(luenta, lista)
    if len(lista) < 1 :
        print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")
    else:
        analyysi = analysoiTiedosto(lista)
        automerkit = analyysi[0]
        lkm = analyysi[1]
        tallennaTiedosto(kirjoitus, automerkit, lkm)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
