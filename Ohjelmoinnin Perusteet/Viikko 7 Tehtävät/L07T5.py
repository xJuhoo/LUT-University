class AUTO:
    Merkki = ""
    Hinta = 0

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Anna auton tiedot")
    print("2) Tulosta autojen tiedot")
    print("3) Tallenna autojen tiedot tiedostoon")
    print("0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta

def kysyTiedot(lista):
    tiedot = AUTO()
    tiedot.Merkki = input("Anna auton merkki: ")
    tiedot.Hinta = int(input("Anna auton hinta: "))
    lista.append(tiedot)
    return lista

def tulostaTiedot(lista):
    print("Listalta löytyy seuraavat autot ja hinnat:")
    for tiedot in lista:
        print(tiedot.Merkki, tiedot.Hinta, end = "")
        print()
    return None

def tallennaTiedot(tiedosto, lista):
    kirjoitus = open(tiedosto, "w", encoding = "utf-8")
    kirjoitus.write("Auton merkki;Auton hinta" + "\n")
    for tiedot in lista:
        kirjoitus.write(tiedot.Merkki + ";" +str(tiedot.Hinta) + "\n")
    kirjoitus.close()
    return None

def paaohjelma():
    lista = []
    tiedosto = input("Anna tallennettavan tiedoston nimi: ")
    print("Tämä ohjelma hallitsee autojen tietoja listalla.")
    while True:
        valinta = valikko()
        if (valinta == 1):
            listaus = kysyTiedot(lista)
        elif (valinta == 2):
            tulostaTiedot(listaus)
        elif (valinta == 3):
            tallennaTiedot(tiedosto, listaus)
            print("Tapahtumat kirjoitettu tiedostoon", ("'" + tiedosto + "'."))
        elif (valinta == 0):
            print("Lopetetaan.")
            lista.clear
            break
        else :
            print("Tuntematon valinta, yritä uudestaan.")
        print()
        
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
