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
# Tehtävä L11T3.py

# eof

def kysyLuku():
    # Tarkistetaan käyttäjän syöte merkkijonon varalta
    while True:
        try:
            luku = int(input("Anna tulostuskertojen määrä: ").strip())
        except ValueError:
            print("Anna kokonaisluku.")
        else:
            break
    
    return luku

def tulostus(sana, luku):
    if luku != 0:
        tulostus(sana, luku - 1)
        print("Sana on", ("'" + sana + "',"), (str(luku) + "."), "kerta.")
    return None

def paaohjelma():
    # Kysytään käyttäjältä tulostettava merkkijono
    sana = input("Anna tulostettava sana: ")
    # Kysytään käyttäjältä luku
    luku = kysyLuku()
    tulostus(sana, luku)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

