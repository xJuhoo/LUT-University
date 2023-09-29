def valikko() :
    print("Valitse haluamasi toiminto:")
    print("1) Syötä tiedot")
    print("2) Laske")
    print("3) Tulosta tulokset")
    print("0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta

def kysyLuku(kehote) :
    luku = int(input(kehote))
    return luku

def summa(luku1, luku2) :
    summa = luku1 + luku2
    return summa

def erotus(luku1, luku2) :
    erotus = luku1 - luku2
    return erotus

def tulostaTulokset(luku1, luku2, Summa, Erotus) :
    print("Luvut ovat", luku1, "ja", str(luku2) + ".")
    print("Lukujen summa on", Summa, "ja erotus on", str(Erotus) + ".")
    return None

def paaohjelma() :
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    while (True) :
        valinta = valikko()
        
        if (valinta == 1) :
            print("Syötä tiedot")
            luku1 = kysyLuku("Anna kokonaisluku 1: ")
            luku2 = kysyLuku("Anna kokonaisluku 2: ")
        elif (valinta == 2) :
            print("Laske")
            Summa = summa(luku1, luku2)
            Erotus = erotus(luku1, luku2)
        elif (valinta == 3) :
            print("Tulosta tulokset")
            tulostus = tulostaTulokset(luku1, luku2, Summa, Erotus)
        elif (valinta == 0) :
            print("Lopetetaan.")
            break
        else :
            print("Tuntematon valinta, yritä uudestaan.")
        print()
    print()
    print("Kiitos ohjelman käytöstä.")
    return None
    
paaohjelma()
