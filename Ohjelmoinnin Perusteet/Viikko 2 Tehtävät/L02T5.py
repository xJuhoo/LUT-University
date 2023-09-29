print("Tämä ohjelma tekee painolle ja pituudelle yksikkömuunnoksia.")
paino = int(input("Anna paino kiloina: "))
naula = round(paino * 2.2046, 1)
print("Paino on",float(paino), "kg eli", naula, "naulaa.")
print()
pituus = int(input("Anna pituus sentteinä: "))
metri = pituus * 0.01
jalka = int(metri * 3.2808)
tuuma = (metri * 39.3700) - (jalka * 12)
print("Pituus on", round(metri, 2), "metriä ", sep=" ", end="")
print("eli amerikkalaisittain", round(float(jalka), 1), "jalkaa ", sep=" ", end="")
print("ja", round(tuuma, 1), "tuumaa.", sep=" ")
print("Kiitos ohjelman käytöstä.")

