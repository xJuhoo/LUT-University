aloitus = int(input("Anna aloitusarvo: "))
lopetus = int(input("Anna lopetusarvo: "))
print()
print("Toteutus for-lauseella:")
for i in range(aloitus, lopetus + 1) :
    print(i, end=" ")
print("\n")
print("Toteutus while-lauseella:")
while aloitus <= lopetus :
    print(aloitus, end=" ")
    aloitus += 1
print("\n")
print("Kiitos ohjelman käytöstä.")
