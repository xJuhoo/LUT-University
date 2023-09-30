import sys

def lueTiedosto(tiedosto, sanakirja):
    try:
        luenta = open(tiedosto, "r")
        koko = luenta.readlines()
        for i in range(0, len(koko)):
            rivi = koko[i].strip()
            if rivi not in sanakirja:
                sanakirja[rivi] = 1
            else:
                sanakirja[rivi] += 1
        luenta.close()
    except Exception:
        print("Tiedoston", ("'" + tiedosto + "'"), "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    lista = sorted(sanakirja.items())
    return lista

def tallennaTiedosto(tiedosto, lista):
    summa = 0
    # Lasketaan kaikkien autojen lukumäärä
    for auto in lista:
        summa += auto[1]
    try:
        open(tiedosto, "w").close() # Tyhjennetään kirjoitettava tiedosto
        kirjoitus = open(tiedosto, "a", encoding = "utf-8")
        kirjoitus.write("Tunnistettiin " + str(len(lista)) + " automerkkiä ja " + str(summa) + " autoa:\n")
        for auto in lista:
            if auto[1] == 1:
                kirjoitus.write(auto[0] + ": " + str(auto[1]) + " auto\n")
            else:
                kirjoitus.write(auto[0] + ": " + str(auto[1]) + " autoa\n")
        kirjoitus.close()
    except Exception:
        print("Tiedoston", ("'" + tiedosto + "'"), "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    
    # Kirjoitetaan tiedot vielä käyttäjälle
    print("Tunnistettiin", len(lista), "automerkkiä ja", summa, "autoa:")
    for auto in lista:
        if auto[1] == 1:
            print(auto[0] + ":", auto[1], "auto")
        else:
            print(auto[0] + ":", auto[1], "autoa")
   
    return None


def paaohjelma():
    automerkit = {}
    luenta = input("Anna luettavan tiedoston nimi: ")
    kirjoitus = input("Anna kirjoitettavan tiedoston nimi: ")
    automerkit = lueTiedosto(luenta, automerkit)
    if len(automerkit) < 1 :
        print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")
    else:
        tallennaTiedosto(kirjoitus, automerkit)
    automerkit.clear()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
