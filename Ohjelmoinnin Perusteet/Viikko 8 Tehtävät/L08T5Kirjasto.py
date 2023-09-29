import sys

# Luokka yksittäiselle varastolle
class VARASTO:
    Tunniste = None
    Lukumaara = None
    Hinta = None

# Aliohjelma tiedostonimen kysymiselle
def kysyTiedosto(kehote):
    nykyinen = ' '
    print("Nykyisen tiedoston nimi on", "'" + nykyinen + "'.")
    uusi = input("Anna uusi " + kehote + " tiedoston nimi: ").strip()
    if not uusi:
        tiedosto = nykyinen
    else:
        tiedosto = uusi
    
    return tiedosto

# Aliohjelma tiedoston lukemiselle
def lueTiedosto(tiedosto, lista):
    try:
        luenta = open(tiedosto, "r", encoding="utf-8")
        koko = luenta.readlines()
        for i in range(0, len(koko)):
        # Luodaan jokaisesta varastosta olio
            varasto = VARASTO()
            rivi = koko[i].replace("\n", "").split(";")
            varasto.Tunniste = rivi[0]
            varasto.Lukumaara = int(rivi[1])
            varasto.Hinta = float(rivi[2])
            lista.append(varasto)
        luenta.close()
        print("Tiedosto", "'" + tiedosto + "'", "luettu,", len(koko), "riviä.")
    except Exception:
        print("Tiedoston", "'" + tiedosto + "'", "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return lista

# Aliohjelma tiedoston analysointiin
def analysoiTiedosto(oliolista, lista):
    for varasto in oliolista:
        summa = varasto.Lukumaara * varasto.Hinta
        lista.append(summa)
    print("Tiedot analysoitu, varastojen yhteisarvo on {0:.2f} EUR.".format(sum(lista)))
    return lista

# Aliohjelma tietojen tallentamiselle
def tallennaTiedot(tiedosto, lista):
    try:
        open(tiedosto, "w", encoding="utf-8").close()
        kirjoitus = open(tiedosto, "a", encoding="utf-8")
        for hinta in lista:
            kirjoitus.write("{0:.2f}\n".format(hinta))
        kirjoitus.close()
        print("Tulokset tallennettu tiedostoon", "'" + tiedosto + "'.")
    except Exception:
        print("Tiedoston", "'" + tiedosto + "'", "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return None
