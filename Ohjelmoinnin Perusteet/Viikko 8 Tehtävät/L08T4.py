import L08T4Kirjasto

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue tiedosto")
    print("2) Analysoi")
    print("3) Kirjoita tiedosto")
    print("0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta

def paaohjelma():
    tiedot = L08T4Kirjasto.TULOS()
    nykyinen = "''"
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    
    while True:
        valinta = valikko()

        if (valinta == 1):
            luenta = L08T4Kirjasto.kysyTiedosto(nykyinen, "Luettavan")
            lista = L08T4Kirjasto.lueTiedosto(luenta)
            print("Tiedosto", ("'" + luenta + "'"), "luettu.")

        elif (valinta == 2):
            analyysi = L08T4Kirjasto.laskeArvot(lista, tiedot)
            print("Analyysi suoritettu.")

        elif (valinta == 3):
            kirjoitus = L08T4Kirjasto.kysyTiedosto(nykyinen, "Kirjoitettavan")
            L08T4Kirjasto.tulostaTiedot(analyysi, kirjoitus)
            print("Tulokset kirjoitettu tiedostoon.")

        elif (valinta == 0):
            print("Lopetetaan")
            break

        else :
            print("Tuntematon valinta, yritä uudestaan.")

        print()
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

