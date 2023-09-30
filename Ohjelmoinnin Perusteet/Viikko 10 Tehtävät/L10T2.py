import sys

def lueTiedosto(tiedosto, sanakirja):
    try:
        luenta = open(tiedosto, "r", encoding = "utf-8")
        koko = luenta.readlines()
        for i in range(1, len(koko)):
            rivi = koko[i].split(";")
            vuosi = rivi[1][0:4]
            if vuosi not in sanakirja:
              sanakirja[vuosi] = 1
            else:
                sanakirja[vuosi] += 1
        luenta.close()
    except Exception:
        print("Tiedoston", ("'" + tiedosto + "'"), "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

    return sanakirja

def tulostaTiedot(sanakirja):
    # Järjestetään sanakirja
    sanakirja = sorted(sanakirja.items(), reverse = True)
    print("Autot lajiteltuna vuosiluvun mukaan laskevaan järjestykseen.")
    print("Vuosi: Autoja")
    summa = 0
    for alkio in sanakirja:
        print(alkio[0] + ":", alkio[1])
        summa += alkio[1]
    print("Yhteensä", summa, "autoa.")
    return None

def paaohjelma():
    autot = {}
    luenta = input("Anna luettavan tiedoston nimi: ")
    autot = lueTiedosto(luenta, autot)
    if len(autot) < 1:
        print("Tiedosto oli tyhjä, yritä uudelleen.")
    else:
        tulostaTiedot(autot)
    autot.clear()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

