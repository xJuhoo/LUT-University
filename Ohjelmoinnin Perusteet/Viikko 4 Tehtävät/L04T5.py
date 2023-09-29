print("Tämä ohjelma etsii luvuilla 5 ja 7 jaollista lukua annetulta lukualueelta.")
aloitus = int(input("Anna lukualueen alaraja: "))
lopetus = int(input("Anna lukualueen yläraja: "))
while (True) :
    if aloitus %5 != 0 :
        print(aloitus, "ei ole jaollinen viidellä, hylätään.")
        aloitus += 1
    elif aloitus %7 != 0 :
        print(aloitus, "ei ole jaollinen seitsemällä, hylätään.")
        aloitus += 1
    if (aloitus %5 == 0 and aloitus %7 == 0) :
        print("Luku", aloitus, "on jaollinen 5:llä ja 7:llä.")
        print("Lopetetaan etsintä.")
        break
    elif aloitus > lopetus :
        print("Alueelta ei löytynyt sopivaa lukua.")
        break
print("Kiitos ohjelman käytöstä.")    
        
