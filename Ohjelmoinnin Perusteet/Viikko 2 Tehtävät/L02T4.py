sana = input("Anna sana: ")
pituus = len(sana)
print("Antamasi sanan kolme ensimmäistä kirjainta ovat", sana[0:3])
print("Sanan neljä viimeistä kirjainta ovat", sana[-4:])
print("Kirjaimet 3, 4, 5 ja 6 ovat", sana[2:6])
print()
print("Sanan joka kolmas kirjain alkaen ensimmäisestä kirjaimesta:", sana[0::3])
print()
sana2 = ("'" + sana + "'")
takaperin = ("'" + sana[::-1] + "'.")
print("Antamasi sana", sana2, "on takaperin", takaperin)
print()
aloitus = int(input("Anna aloituspaikka: "))
lopetus = int(input("Anna lopetuspaikka: "))
siirtyma = int(input("Anna siirtymä: "))
print("Antamillasi asetuksilla sana", sana, "tulostuu näin:", sana[aloitus:lopetus:siirtyma])
print()
print("Antamasi sanan pituus oli", pituus, "merkkiä.")
print("Kiitos ohjelman käytöstä.")
