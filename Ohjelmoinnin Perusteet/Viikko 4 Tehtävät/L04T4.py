print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
while (True) :
    print("Valitse haluamasi toiminto:")
    print("1) Syötä tiedot")
    print("2) Laske")
    print("3) Tulosta tulokset")
    print("0) Lopeta")
    valinta = input("Anna valintasi: ")
    if valinta == "1" :
        print("Syötä tiedot")
        luku1 = int(input("Anna luku 1: "))
        luku2 = int(input("Anna luku 2: "))
    elif valinta == "2" :
        print("Laske")
        summa = luku1 + luku2
    elif valinta == "3" :
        print("Tulosta tulokset")
        print("Lukujen summa on", str(summa) + ".")
    elif valinta == "0" :
        print("Lopetetaan.")
        break
    else :
        print("Tuntematon valinta, yritä uudestaan.")
    print()
print()
print("Kiitos ohjelman käytöstä.")
