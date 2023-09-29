print("Ohjelma kysyy merkkijonoja ja etsii niistä pisimmän.")
lukumaara = int(input("Kuinka monta merkkijonoa kysytään: "))
minpituus = int(input("Mikä on merkkijonon minimipituus: "))
merkki = input("Mitä merkkiä merkkijonossa ei saa olla: ")
summa = 0 # Laskee syötettyjen merkkijonojen määrää.
pituus = 0 # Tallennetaan pisimmän sanan pituus tähän.
pisinsana = "0" # Tallennetaan pisin sana tähä.
while (True) :
    jono = input("Anna merkkijono: ")
    summa += 1
    if len(jono) > pituus :
        pituus = len(jono)
        pisinsana = jono
    if merkki in jono :
        print("Ohjelma päättyi, koska merkkijonossa oli kielletty merkki.")
        break
    if len(jono) < minpituus :
        print("Ohjelma päättyi, koska merkkijonon minimipituus ei täyttynyt.")
        break
    if summa == lukumaara :
        print("Ohjelma päättyi, koska maksimimäärä merkkijonoja tuli täyteen.")
        break
print("Annoit", str(summa), "merkkijonoa.")
print("Pisin merkkijono oli", ("'" + pisinsana + "',"), "jossa oli", pituus, "merkkiä.")
print("Kiitos ohjelman käytöstä.")
