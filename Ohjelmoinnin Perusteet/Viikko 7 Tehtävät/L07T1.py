######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Juho Rekonen
# Opiskelijanumero:441410
# Päivämäärä: 20.10.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L07T1.py

# eof

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lisää tuote listaan")
    print("2) Poista tuote listasta")
    print("0) Lopeta")
    valinta = int(input("Valintasi: "))
    return valinta

def paaohjelma():
    ostoslista = []
    while True:
        print("Ostoslistasi sisältää seuraavat tuotteet:")
        for i in ostoslista:
            print(i, end = " ")
        print()
        valinta = valikko()
        if valinta == 1:
            tuote = input("Anna lisättävä tuote: ")
            ostoslista.append(tuote)
            tuote = ""
        elif valinta == 2:
            print("Ostoslistassasi on", len(ostoslista), "tuotetta.")
            poisto = int(input("Anna poistettavan tuotteen järjestysnumero: "))
            if poisto == 0:
                print("Tuotteiden järjestysnumerot alkavat numerosta 1.")
            elif poisto > len(ostoslista):
                print("Indeksiä", poisto, "ei löydy.")
            else :
                del ostoslista[poisto - 1]
        elif valinta == 0:
            print("Lopetetaan")
            print("Sinulta jäi ostamatta seuraavat tuotteet:")
            for i in ostoslista:
                print(i, end = " ")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
    print("\n")
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
