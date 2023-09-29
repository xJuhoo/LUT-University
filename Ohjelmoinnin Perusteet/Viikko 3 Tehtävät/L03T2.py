print("Selvitetään sanojen aakkosjärjestys.")
sana1 = input("Anna sana 1: ")
sana2 = input("Anna sana 2: ")
if sana1 < sana2 :
    print(("'" + sana1 + "'"), "on aakkosissa aiemmin kuin", ("'" + sana2 + "'."))
elif sana1 > sana2 :
    print(("'" + sana2 + "'"), "on aakkosissa aiemmin kuin", ("'" + sana1 + "'."))
else :
    print("Sanat ovat samoja,", ("'" + sana1 + "'."))
print()
print("Selvitetään merkin sisältyminen merkkijonoon.")
jono = input("Anna merkkijono: ")
merkki = input("Anna etsittävä merkki: ")
if merkki in jono :
    print("Merkki", ("'" + merkki + "'"), "sisältyy merkkijonoon", ("'" + jono + "'."))
else :
    print("Merkki", ("'" + merkki + "'"), "ei sisälly merkkijonoon", ("'" + jono + "'."))
print()
print("Selvitetään, onko sana palindromi.")
sana3 = input("Anna testattava sana: ")
if sana3 == sana3[: : -1] :
    print("Sana", ("'" + sana3 + "'"), "on palindromi.")
else :
    print("Sana ei ole palindromi.")
    print("Sana on etuperin", ("'" + sana3 + "'"), "ja takaperin", ("'" + sana3[: : -1] + "'."))
print("Kiitos ohjelman käytöstä.")
