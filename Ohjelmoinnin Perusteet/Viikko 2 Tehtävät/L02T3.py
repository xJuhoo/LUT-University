print("Tämä ohjelma laskee neljän tenttiarvosanan keskiarvon.")
a = int(input("Anna 1. tenttiarvosana väliltä 0-5: "))
b = int(input("Anna 2. tenttiarvosana väliltä 0-5: "))
c = int(input("Anna 3. tenttiarvosana väliltä 0-5: "))
d = int(input("Anna 4. tenttiarvosana väliltä 0-5: "))
ka = (a + b + c + d)/4
print()
summa = str(a + b + c + d) + "."
pyoristys = str(round(ka, 1)) + "."
kokonaisluku = str(int(ka)) + "."
print("Antamiesi arvosanojen summa on", summa)
print("Antamiesi arvosanojen keskiarvo on", pyoristys)
print("Keskiarvo on kokonaislukuna", kokonaisluku)
print("Kiitos ohjelman käytöstä.")

