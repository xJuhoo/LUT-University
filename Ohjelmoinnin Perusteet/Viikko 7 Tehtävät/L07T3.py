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
# Tehtävä L07T3.py

# eof

def paaohjelma():
    tiedosto = input("Anna tiedoston nimi: ")
    luenta = open(tiedosto, "r", encoding = "utf-8")
    print("Kalastuskilpailun tulokset ovat seuraavat:")
    koko = luenta.readlines()
    for i in range(0, len(koko)):
        rivi = koko[i].replace("\n", "")
        if "Joukkkue" not in rivi: # Skipataan ensimmäinen rivi.
            lista = rivi.split(";")
            print("Joukkue", ("'" + lista[0] + "'"), "sai kalan", lista[1] + ",", "joka oli", lista[2], "cm.")
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
    
    
    
