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
# Tehtävä L11T1.py

# eof
def kysyLuku():
    # Tarkistetaan käyttäjän antama syöte merkkijonojen varalta
    while True:
        try:
            luku = int(input("Anna luku: ").strip())
        except ValueError:
            print("Anna kokonaisluku.")
        else:
            break
    
    return luku

def neliojuuri(luku):
    # Tarkistetaan, onko annettu luku 1
    if luku == 1:
        return luku
    else:
        aloitus = 1
        askel = 0.5
        while aloitus < luku ** 0.5:
            aloitus += askel
    
    return aloitus

def paaohjelma():
    # Kysytään käyttäjältä luku
    luku = kysyLuku()
    nelio = neliojuuri(luku)
    print("Neliöjuuri on", round(nelio))
    print("Kiitos ohjelman käytöstä.")
    return None


paaohjelma()

