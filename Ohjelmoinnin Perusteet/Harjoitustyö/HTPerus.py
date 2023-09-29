######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Juho Rekonen
# Opiskelijanumero:441410
# Päivämäärä: 6.11.2022 - 11.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä HTPerus.py

# eof

# Tuodaan kirjasto, sen aliohjelmat ja luokat
import HTPerusKirjasto

# Valikkopohjainen aliohjelma
def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue tiedosto")
    print("2) Analysoi")
    print("3) Kirjoita tiedosto")
    print("4) Analysoi viikonpäivittäiset keskiarvot")
    print("0) Lopeta")
    # Tarkistetaan käyttäjän antama syöte merkkijonojen tai kirjotusvirheiden varalta
    while True:
        try: # Kysytään käyttäjältä syöte ja muutetaan se kokonaisluvuksi
            valinta = int(input("Anna valintasi: "))
        except ValueError:
            print("Anna valinta kokonaislukuna.")
        else: # Mikäli erroria ei synny, hypätään ulos loopista ja palautetaan valinta pääohjelmaan
            break

    return valinta

# Pääohjelma
def paaohjelma():
    tuntidata = [] # Tähän listaan tunnit ja tuntikohtaiset hinnat
    paivadata = [] # Tähän listaan päivät ja päivittäiset keskiarvohinnat
    viikonpaivadata = [] # Tähän listaan viikonpäivittäiset keskiarvohinnat

    # Valintojen yhteydessä tiettyjen listojen tyhjennys, jotta voidaan käsitellä aina yhtä tiedostoa kerrallaan
    while True:
        valinta = valikko()

        if valinta == 1:
            tuntidata.clear()
            luenta = HTPerusKirjasto.kysyTiedosto("luettavan")
            # Syötetään aliohjelmaan tyhjä lista ja palautetaan tiedot sisältävä lista
            tuntidata = HTPerusKirjasto.lueTiedosto(luenta, tuntidata)
        
        elif valinta == 2:
            paivadata.clear()
            # Tarkistetaan, onko tiedoston lukua suoritettu
            if len(tuntidata) < 1:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
            else:
                # Haetaan tilastoitavat tiedot sisältävä olio
                tilasto = HTPerusKirjasto.tilastoiTiedot(tuntidata)
                # Sekä oliolista, joka sisältää päivät ja päiväkohtaiset keskiarvohinnat
                paivadata = HTPerusKirjasto.analysoiTiedosto(tuntidata, paivadata)

        elif valinta == 3:
            # Tarkistetaan, onko analyysiä suoritettu
            if len(paivadata) < 1:
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")
            else:
                kirjoitus = HTPerusKirjasto.kysyTiedosto("kirjoitettavan")
                # Kirjoittavan aliohjelman saamat parametrit: (kirjoitustapa, tiedosto, lista, olio)
                HTPerusKirjasto.kirjoitaTiedosto(1, kirjoitus, paivadata, tilasto)
        
        elif valinta == 4:
            viikonpaivadata.clear()
            # Tarkistetaan, onko tiedoston lukua suoritettu
            if len(tuntidata) < 1:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
            else:
                kirjoitus2 = HTPerusKirjasto.kysyTiedosto("kirjoitettavan")
                viikonpaivadata = HTPerusKirjasto.viikonpaivat(tuntidata, viikonpaivadata)
                # Viikonpäiviä kirjoittaessa oliota ei tarvita, alustetaan se arvolle None
                HTPerusKirjasto.kirjoitaTiedosto(2, kirjoitus2, viikonpaivadata, None)
        
        elif valinta == 0:
            print("Lopetetaan.")
            # Ohjelman loppuessa kaikkien listojen tyhjennys
            tuntidata.clear()
            paivadata.clear()
            viikonpaivadata.clear()
            break
            
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        
        print()
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

