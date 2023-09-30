import L09T4Kirjasto

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue tiedosto")
    print("2) Analysoi")
    print("3) Kirjoita tiedosto")
    print("0) Lopeta")
    
    while True:
        try:
            valinta = input("Anna valintasi: ")
            return int(valinta)
        except ValueError:
            print("Anna valinta kokonaislukuna.")
    
    return None

def paaohjelma():
    tiedot = L09T4Kirjasto.TULOS()
    nykyinen = "''"
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    lista = None
    analyysi = None

    while True:
        valinta = valikko()

        if (valinta == 1):
            luenta = L09T4Kirjasto.kysyTiedosto(nykyinen, "Luettavan")
            lista = L09T4Kirjasto.lueTiedosto(luenta)
            print("Tiedosto", ("'" + luenta + "'"), "luettu.")

        elif (valinta == 2):
            if lista == None:
                print("Ei analysoitavia tietoja, ei analysoitu.")
            else:
                analyysi = L09T4Kirjasto.laskeArvot(lista, tiedot)
                print("Analyysi suoritettu.")

        elif (valinta == 3):
            if analyysi == None:
                print("Ei tallennettavia tietoja, tiedostoa ei tallennettu.")
            else: 
                kirjoitus = L09T4Kirjasto.kysyTiedosto(nykyinen, "Kirjoitettavan")
                L09T4Kirjasto.tulostaTiedot(analyysi, kirjoitus)
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

