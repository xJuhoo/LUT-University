print("Anna kaksi kokonaislukua.")
luku1 = int(input("Anna luku 1: "))
luku2 = int(input("Anna luku 2: "))
print("Selvitetään, ovatko antamasi luvut parillisia.")
if luku1 %2 == 0 :
    print("Luku", luku1, "on parillinen.")
else :
    print("Luku", luku1, "on pariton.")
if luku2 %2 == 0 :
    print("Luku", luku2, "on parillinen.")
else :
    print("Luku", luku2, "on pariton.")
print("Selvitetään, kumpi antamistasi luvuista on pienempi.")
if luku1 < luku2 :
    print("Luku", luku1, "on pienempi.")
elif luku1 > luku2 :
    print("Luku", luku2, "on pienempi.")
else :
    print("Luvut", luku1, "ja", luku2, "ovat yhtäsuuria.")
print("Kiitos ohjelman käytöstä.")
