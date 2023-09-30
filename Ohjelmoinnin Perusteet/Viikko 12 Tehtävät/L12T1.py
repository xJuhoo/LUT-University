def hloTunnus():
    tunnus = input("Anna henkilötunnus: ").upper()
    return tunnus

def validointi(tunnus):
    sanakirja = {
        "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9, "10": "A", "11": "B",
        "12": "C", "13": "D", "14": "E", "15": "F", "16": "H", "17": "J",
        "18": "K", "19": "L", "20": "M", "21": "N", "22": "P", "23": "R",
        "24": "S", "25": "T", "26": "U", "27": "V", "28": "W", "29": "X", "30": "Y" 
    }

    try:
        paatos = None # Alustus arvolle None
        jakojaannos = int(tunnus[0:6] + tunnus[7:10]) % 31
        # Tarkistetaan ensin annetun henkilötunnuksen pituus
        if len(tunnus) != 11:
            paatos = False
        
        # Päivän tulee olla luku väliltä 1 - 31
        elif (int(tunnus[0:2]) <= 0) or (int(tunnus[0:2]) > 31):
            paatos = False
        
        # Kuukauden tulee olla luku väliltä 1 - 12
        elif (int(tunnus[2:4]) <= 0) or (int(tunnus[2:4]) > 12):
            paatos = False
        
        #Vuoden tulee olla luku väliltä 0 - 99
        elif (int(tunnus[4:6]) < 0) or (int(tunnus[4:6]) > 99):
            paatos = False

        # Tarkistetaan vuosisadan tunnus
        elif tunnus[6] not in ["-", "+", "A"]:
            paatos = False

        # Tarkistetaan vuositunnuksen jälkeen tuleva luku
        elif (int(tunnus[-4:-1]) < 2) or (int(tunnus[-4:-1]) > 899):
            paatos = False

        # Tarkistetaan tarkistusmerkki
        elif tunnus[-1].isalpha() == False:
            paatos = False

        # Tarkistetaan, onko tarkistusmerkki oikea
        elif tunnus[-1] != sanakirja[str(jakojaannos)]:
            paatos = False
            
        # Muussa tapauksessa henkilötunnus hyväksytään
        else:
            paatos = True

    except ValueError:
        pass

    return paatos


def paaohjelma():
    tunnus = hloTunnus()
    paatos = validointi(tunnus)
    if paatos:
        print("Henkilötunnus hyväksytty.")
    else:
        print("Henkilötunnusta ei hyväksytä.")
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

