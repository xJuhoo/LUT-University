# Tuodaan kirjasto, sen luokat ja aliohjelmat
import L08T5Kirjasto

# Valikkopohjainen aliohjelma
def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue tiedosto")
    print("2) Analysoi tiedot")
    print("3) Tallenna tulokset")
    print("0) Lopeta")

    # Tarkistetaan käyttäjän antama syöte merkkijonojen tai kirjotusvirheiden varalta
    while True:
        try:
            valinta = int(input("Anna valintasi: ").strip())
        except ValueError:
            print("Anna valinta kokonaislukuna.")
        else: # Mikäli erroria ei synny, hypätään ulos loopista ja palautetaan valinta pääohjelmaan.
            break
    
    return valinta

# Pääohjelma
def paaohjelma():
    Varastot = [] # Oliolista varastoille
    Hinnat = [] # Lista, johon varastojen hinnat tallentamista varten

    while True:

        valinta = valikko()

        if valinta == 1:
            Varastot.clear()
            luenta = L08T5Kirjasto.kysyTiedosto("luettavan")
            Varastot = L08T5Kirjasto.lueTiedosto(luenta, Varastot)
        
        elif valinta == 2:
            Hinnat.clear()
        # Tarkistetaan, onko tiedoston lukua suoritettu
            if len(Varastot) < 1:
                print("Ei tietoja analysoitavaksi, lue tiedosto ennen analyysiä.")
            else:
                Hinnat = L08T5Kirjasto.analysoiTiedosto(Varastot, Hinnat)

        elif valinta == 3:
        # Tarkistetaan, onko analyysiä suoritettu
            if len(Hinnat) < 1:
                print("Ei tietoja tallennettavaksi, analysoi tiedosto ennen tallentamista.")
            else:
                kirjoitus = L08T5Kirjasto.kysyTiedosto("kirjoitettavan")
                L08T5Kirjasto.tallennaTiedot(kirjoitus, Hinnat)

        elif valinta == 0:
        # Ohjelman loppuessa listojen tyhjennys
            Varastot.clear()
            Hinnat.clear()
            print("Lopetetaan.")
            break

        else:
            print("Tuntematon valinta, yritä uudelleen.")
        
        print()
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()


