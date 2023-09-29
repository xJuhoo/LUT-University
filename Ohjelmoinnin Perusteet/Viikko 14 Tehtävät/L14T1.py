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
# Tehtävä L14T1.py

# eof

def paaohjelma():
    km = int(input("Anna vuotuiset kilometrit: "))
    kulutus = float(input("Anna moottorin polttoaineen kulutus (l/100km): "))
    hinta = float(input("Anna polttoaineen hinta (€/l): "))
    ika = int(input("Anna auton ikä vuosissa: "))
    vakuutus = int(input("Anna vakuutusten määrä (euroissa): "))
    bonus = int(input("Anna bonusprosentti kokonaislukuna: "))
    verot = int(input("Anna verojen määrä: "))
    yhteensa = 0
    for i in range(1, 6):
        summa = km / 100 * kulutus * hinta + (vakuutus - 0.01 * bonus * vakuutus) + verot + 200 * pow(ika, 0.5)
        print("{}. vuosi: {}".format(i, round(summa)))
        ika += 1
        yhteensa += summa
    print("Viiden vuoden aikana autoon käytettiin rahaa {} euroa.".format(round(yhteensa)))
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

