def kirjoitaData(tiedosto, s) :
    tiedosto.write(s)
    return None
      
def paaohjelma() :
    tiedosto1 = input("Anna luettavan tiedoston nimi: ")
    tiedosto2 = input("Anna tallennettavan tiedoston nimi: ")
    open(tiedosto2, "w").close() # Tyhjennetään kirjoitustiedosto
    
    kirjoitus = open(tiedosto2, "a") # Avataan uudelleen ilman tyhjentämistä
    otsikko = "{:>10}:{:>5}\n".format("Pvm", "kWh")
    kirjoitus.write(otsikko) # Kirjoitetaan aluksi vain otsikko
    
    luenta = open(tiedosto1, "r")
    rivi = luenta.readline() # Luetaan tiedostoa rivi kerrallaan
    rivi1 = True # Alustetaan tiedoston ensimmäinen rivi arvolle True
    kWhfloat = 0.0 # Sähkönkulutusarvo float - muodossa
    kWh = 0 # ja tallentamista varten int - muodossa
    pvm = ""
    while len(rivi) > 0: # Näin saadaan lopetettua ennen viimeistä riviä
        if "A" not in rivi: # ja näin skipataan ensimmäinen rivi.
            rivi1 = False
            pvm = rivi[0:10]
            yo = float(rivi[14:18]) # Lasketaan erikseen yö ja päiväarvot
            paiva = float(rivi[19:23])
            kWhfloat = kWhfloat + yo + paiva
            kWh = int(round(kWhfloat,0))
        
        rivi = luenta.readline()
        tarkistus = rivi[0:10] # Tarkistetaan jos päivämäärä vaihtuu
        if pvm != tarkistus:
            if rivi1 == False:
                s = "{:>10}:{:>5}\n".format(pvm, kWh)
                kirjoitaData(kirjoitus, s)
            kWhfloat = 0
            kWh = 0
                
    luenta.close()
    kirjoitus.close()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
