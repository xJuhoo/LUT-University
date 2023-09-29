def valikko() :
    print("Valitse haluamasi toiminto:")
    print("1) Anna tiedostonimet")
    print("2) Analysoi")
    print("3) Kirjoita tiedosto")
    print("0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta

def kysyTiedosto(tiedosto, kehote) :
    print(kehote + "tiedoston nimi on", tiedosto + ".")
    uusi = input("Anna uusi nimi, enter säilyttää nykyisen: ")
    if not uusi :
        return None
    else :
        return uusi

def laskeArvot(tiedosto) :
    file = open(tiedosto, "r")
    numerot = {int(i) for i in file}
    suurin = max(numerot)
    pienin = min(numerot)
    return suurin, pienin

def kirjoitaTiedosto(tiedosto, suurin, pienin) :
    kirjoitus = open(tiedosto, "w")
    kirjoitus.write("Analyysin tulokset ovat seuraavat:" + "\n")
    kirjoitus.write("Datan pienin arvo on " + str(pienin) + "." + "\n")
    kirjoitus.write("Datan suurin arvo on " + str(suurin) + "." + "\n")
    kirjoitus.close()
    return None

def paaohjelma() :
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    vanha = "''"
    while (True) :
        valinta = valikko()
        
        if (valinta == 1) :
            print("Anna tiedostonimet")
            uusi1 = kysyTiedosto(vanha, "Luettavan ")
            uusi2 = kysyTiedosto(vanha, "Kirjoitettavan ")
            
        elif (valinta == 2) :
            print("Suoritetaan analyysi")
            arvot = laskeArvot(uusi1)
            
        elif (valinta == 3) :
            print("Kirjoitetaan tulokset tiedostoon")
            kirjoitaTiedosto(uusi2, arvot[0], arvot[1])
            
        elif (valinta == 0) :
            print("Lopetetaan")
            break
        
        else :
            print("Tuntematon valinta, yritä uudestaan.")
        print()
    print()
    print("Kiitos ohjelman käytöstä.")
    return None
    
paaohjelma()
