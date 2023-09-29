######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Juho Rekonen
# Opiskelijanumero: 441410
# Päivämäärä: 20.10.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L07T2.py

# eof

class TILI:
    Nimi = ""
    Saldo = 0


def kysyTiedot(hlo):
    hlo.Nimi = input("Anna pankkitilin nimi: ")
    hlo.Saldo = round(float(input("Anna pankkitilin saldo: ")), 2)
    return hlo.Nimi, hlo.Saldo

def tallennaTiedot(nimi, saldo):
    print("Pankkitilillä", ("'" + nimi + "'"), "on nyt rahaa", str(saldo) + "e.")
    return None

def paaohjelma():
    hlo = TILI()
    tilitiedot = kysyTiedot(hlo)
    tallennaTiedot(tilitiedot[0], tilitiedot[1])
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

    
    
