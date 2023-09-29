######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Juho Rekonen
# Opiskelijanumero:441410
# Päivämäärä: 6.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T2Kirjasto.py

# eof

# Luodaan tähän aliohjelmat.

def litraG(tilavuus): # Litroista galloneiksi
    gallon = (tilavuus / 3.79)
    return gallon

def litraP(tilavuus): # Litroista pinteiksi
    pint = (tilavuus / 0.47)
    return pint

def litraC(tilavuus): # Litroista cupeiksi
    cup = (tilavuus / 0.24)
    return cup

def litraFO(tilavuus): # Litroista fluid ounceiksi
    FluidOunce = (tilavuus / 0.0296)
    return FluidOunce

def GallonL(tilavuus): # Galloneista litroiksi
    litra = (tilavuus * 3.79)
    return litra

def PintL(tilavuus): # Pinteistä litroiksi
    litra = (tilavuus * 0.47)
    return litra

def CupL(tilavuus): # Cupeista litroiksi
    litra = (tilavuus * 0.24)
    return litra

def FluidOunceL(tilavuus): # Fluid ounceista litroiksi
    litra = (tilavuus * 0.0296)
    return litra

versio = 1.0

