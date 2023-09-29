print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
print("Valitse haluamasi toiminto:")
print("1) Tulosta merkkijono etuperin")
print("2) Tulosta merkkijono takaperin")
print("3) Tulosta merkkijonon pituus")
print("0) Lopeta")
valinta = input("Anna valintasi: ")
if valinta == "0" : #Ohjelma loppuu!
    0
else :
    jono = input("Anna merkkijono: ")
    if valinta == "1" :
        print("Merkkijono on etuperin", ("'" + jono + "'."))
    elif valinta == "2" :
        print("Merkkijono on takaperin", ("'" + jono[: : -1] + "'."))
    elif valinta == "3" :
        print("Merkkijonon pituus on", (str(len(jono)) + "."))
    else :
        print("Tuntematon valinta.")
    print("Kiitos ohjelman käytöstä.")
