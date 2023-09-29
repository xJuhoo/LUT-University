def tarkistaRivi(rivi):
    siistirivi = rivi.lower()
    erikoismerkit = "! #¤%&/-()*:;.,\"?^+" # Luodaan muuttuja, jotta voidaan testata kerralla kaikki erikoismerkit.
    while True :
        if len(siistirivi) < 3 :
            siistirivi = "epätosi"
            break

        if any(i.isdigit() for i in siistirivi) :
            siistirivi = "epätosi"
            break
        for i in erikoismerkit :
            siistirivi = siistirivi.replace(i, "")
        if siistirivi == siistirivi[ : : -1] :
            break
        else :
            break
              
    return rivi, siistirivi

def tiedostoKirjoita(kirjoitus, rivi, siistirivi) :
    while True :
        kirjoitus.write(rivi + "\n")
        kirjoitus.write("----> " + siistirivi + "\n")
        break
    return None

def paaohjelma():
    tiedosto1 = input("Anna luettavan tiedoston nimi: ")
    tiedosto2 = input("Anna kirjoitettavan tiedoston nimi: ")
    kirjoitus = open(tiedosto2, "w", encoding = "utf-8") # Avataan kirjoitustiedosto
    luenta = open(tiedosto1, "r", encoding = "utf-8")
    rivi = luenta.readlines() # Näin saadaan luettavan tiedoston pituus
    for i in range(0, len(rivi)) :
        rivi[i] = rivi[i].replace("\n", "") # Poistetaan rivin lopusta rivinvaihtomerkki
        tarkistus = tarkistaRivi(rivi[i])
        if tarkistus[1] == (tarkistus[1])[::-1] : # Tarkistetaan jos siistitty muoto on sama molemmin päin
            print("OK:", ("'" + rivi[i] + "'"))
            tiedostoKirjoita(kirjoitus, rivi[i], tarkistus[1])
        else :
            print("Ei OK:", ("'" + rivi[i] + "'"))

    kirjoitus.close() # Suljetaan kirjoitustiedosto
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
