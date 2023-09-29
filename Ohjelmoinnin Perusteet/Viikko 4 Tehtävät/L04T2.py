paino = float(input("Anna paino väliltä 30-130 kg (0 lopettaa): "))
summa = 0
lukumaara = 0
while (True) :
    if 30 <= paino <= 130 :
        summa += paino
        paino = float(input("Anna paino väliltä 30-130 kg (0 lopettaa): "))
        lukumaara += 1
    elif paino == 0 :
        break
    else :
        print("Väärä syöte. Painon tulee olla 30 ja 130 kg välillä (0 lopettaa).")
        paino = float(input("Anna paino väliltä 30-130 kg (0 lopettaa): "))
print("Painojen keskiarvo on", str(round(summa / lukumaara, 1)) + ".")
print("Kiitos ohjelman käytöstä.")
