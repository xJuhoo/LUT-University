######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Juho Rekonen
# Opiskelijanumero:441410
# Päivämäärä: 28.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L12T2.py

# eof

def kysyLuku(kehote):
    luku = input("Anna " + kehote + " binaariluku: ")
    return luku

def muunnos(luku):
    tulos = 0
    for i in luku:
        tulos = tulos*2 + int(i)
    print("Bittijonosi", luku, "on kymmenkantaisena kokonaislukuna", tulos)
    return tulos

def erotus(ekaluku, tokaluku):
    erotus = ekaluku - tokaluku
    print("Lukujen", ekaluku, "ja", tokaluku, "erotus on", erotus)
    return None

def paaohjelma():
    ekaluku = kysyLuku("ensimmäinen")
    tokaluku = kysyLuku("toinen")
    # Muunnetaan binaariluvut kokonaisluvuiksi
    ekamuunnos = muunnos(ekaluku)
    tokamuunnos = muunnos(tokaluku)
    # Suoritetaan erotus
    erotus(ekamuunnos, tokamuunnos)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

