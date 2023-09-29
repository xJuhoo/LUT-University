print("Selvitetään tuotteen alennusprosentti ja hinta.")
hinta = float(input("Mikä tuotteen hinta on: "))
print("Lasketaanko hinta")
print("1) yhdellä monihaaraisella valintarakenteella")
print("2) useilla erillisillä valintarakenteilla?")
valinta = input("Anna valintasi: ")
if valinta == "1" :
    alennus = 0
    print("Yhdellä monihaaraisella valintarakenteella tulokset ovat seuraavat:")
    if hinta > 300 :
        alennus = 30
        hinta = hinta * 0.70
    elif hinta > 200 :
        alennus = 20
        hinta = hinta * 0.80
    elif hinta > 100 :
        alennus = 10
        hinta = hinta * 0.90
    print("Tuotteen alennus on", (str(alennus) + "%"), "ja hinnaksi jää", (str(round(hinta, 2)) + "e."))
elif valinta == "2" :
    alennus = 0
    print("Monella erillisellä valintarakenteella tulokset ovat seuraavat:")
    if hinta > 300 :
        alennus = 30
        hinta = hinta * 0.70
        if hinta > 200 :
            alennus = 20
            hinta = hinta * 0.80
            if hinta > 100 :
                alennus = 10
                hinta = hinta * 0.90
    elif hinta > 200 :
        alennus = 20
        hinta = hinta * 0.80
        if hinta > 100 :
            alennus = 10
            hinta = hinta * 0.90
    elif hinta > 100 :
        alennus = 10
        hinta = hinta * 0.90
    print("Tuotteen alennus on", (str(alennus) + "%"), "ja hinnaksi jää", (str(round(hinta, 2)) + "e."))
else :
    print("Tuntematon valinta.")
print("Kiitos ohjelman käytöstä.")
