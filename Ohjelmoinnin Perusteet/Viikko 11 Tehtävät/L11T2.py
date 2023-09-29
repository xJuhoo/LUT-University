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
# Tehtävä L11T2.py

# eof

def kysyLuku():
    # Tarkistetaan käyttäjän syöte merkkijonojen varalta
    while True:
        try:
            luku = int(input("Anna kuukausien lukumäärä: ").strip())
        except ValueError:
            print("Anna kokonaisluku.")
        else:
            break
    
    return luku

def Fibonacci(luku, dict):
    if luku in dict:
        return dict[luku]
    if (luku <= 2):
        return 1
    dict[luku] = Fibonacci(luku - 1, dict) + Fibonacci(luku - 2, dict)
    return dict[luku]
    

def paaohjelma():
    dict = {}
    # Kysytään käyttäjältä kuukausien määrä
    kuukaudet = kysyLuku()
    # Tarkistetaan, jos käyttäjän antama luku on ei-positiivinen  
    lukumaara = Fibonacci(kuukaudet, dict)
    print("Kanipariskuntia on", kuukaudet, "kuukauden kuluttua", lukumaara)
    print("Kiitos ohjelman käytöstä.")

paaohjelma()
