######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Juho Rekonen
# Opiskelijanumero:441410
# Päivämäärä: 6.11.2022 - 11.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä HTPerusKirjasto.py

# eof
import datetime
import sys

# Luokka yksittäiselle riville
class TUNTI():
    aika = None # Päivämäärä + kellonaika
    hinta = None # Tuntikohtainen hinta

# Luokka yksittäiselle päivälle
class PAIVA():
    paivamaara = None # Päivämäärä
    kahinta = None # Päivittäinen keskiarvohinta

# Luokka, johon tallennetaan tiedoston tilastot
class TILASTO():
    lukumaara = None # Kaikkien hintojen lukumäärä
    keskiarvo = None # Kaikkien hintojen keskiarvo
    kallein = None # Sähkön kallein hinta
    kalleinaika = None # Aika, jolloin hinta kallein
    halvin = None # Sähkön halvin hinta
    halvinaika = None # Aika, jolloin hinta halvin

# Aliohjelma tiedostonimen kysymiselle
def kysyTiedosto(kehote):
    tiedosto = input("Anna " + kehote + " tiedoston nimi: ")
    return tiedosto

# Aliohjelma luettavan tiedoston lukemiselle
def lueTiedosto(tiedosto, lista):
    try:
        luenta = open(tiedosto, "r")
        koko = luenta.readlines()
        # Tiedoston viimeinen rivi on tyhjä rivi, joten 'range'-funktiolla mentäessä viimeiseen riviin asti se jää käymättä 
        for i in range(1, len(koko)): # Aloitetaan arvosta 1, jolloin skipataan otsikkorivi
            # Luodaan jokaisesta tunnista olio
            tunti = TUNTI()
            # Rivi kerrallaan erotellaan data ';' merkin kohdalta + poistetaan rivinvaihto
            rivi = koko[i].replace("\n", "").split(";")
            tunti.hinta = rivi[1] # Rivi jaetaan kahteen alkioon, joista jälkimmäinen kertoo hinnan
            # Aikaleimaa varten poistetaan vielä hipsut
            aikaleima = datetime.datetime.strptime(rivi[0].replace("\"", ""), "%Y-%m-%d %H:%M:%S")
            tunti.aika = aikaleima.strftime("%d.%m.%Y %H:%M") # Muutetaan suoraan päivämäärään erottimeksi piste
            lista.append(tunti) # Lisätään oliot listaan
        print("Tiedosto", ("'" + tiedosto + "'"), "luettu.")
        luenta.close()

    except Exception:
        print("Tiedoston", ("'" + tiedosto + "'"), "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    
    return lista

# Aliohjelma päivittäisten keskiarvojen laskemiseen
def analysoiTiedosto(tuntidata, paivadata):
    summa = 0
    hinta = 0.0
    # Muodostetaan tarkistuspäivämäärä, jolla tutkitaan päivämäärän vaihtumista
    tpvm = datetime.datetime.strptime("01.01.2021", "%d.%m.%Y") # Alustetaan vuoden ensimmäiselle päivälle
    tarkistus = tpvm.strftime("%d.%m.%Y")
    for tunti in tuntidata: # Käydään tuntidataa (oliolistaa) läpi alkio kerrallaan
        paiva = PAIVA() # Luodaan jokaisesta päivämäärästä oma olio
        pvm = tunti.aika[0:10]

    # Tutkitaan onko päivämäärä vaihtunut
        if tarkistus != pvm:
            paiva.kahinta = hinta / summa
            paiva.paivamaara = tarkistus
            tarkistus = pvm
            paivadata.append(paiva) # Lisätään päivä oliolistaan
            hinta = float(tunti.hinta)
            summa = 1 # Summaksi alustetaan 1, koska päivän vaihtuessa uutta päivää on jo 1 kpl
        
    # Tutkitaan erikseen tapaus, jossa päästään viimeiseen päivämäärään
        elif tarkistus == pvm and tunti == tuntidata[-1]:
            hinta += float(tunti.hinta)
            summa += 1
            paiva.kahinta = hinta / summa
            paiva.paivamaara = tarkistus
            paivadata.append(paiva) # Lisätään päivä oliolistaan

    # Jos tarkistus on sama kuin päivämäärä
        elif tarkistus == pvm:
            hinta += float(tunti.hinta)
            summa += 1

        else:
            continue
    
    print("Tilastotietojen analyysi suoritettu", len(tuntidata), "alkiolle.")
    print("Päivittäiset keskiarvot laskettu", len(paivadata), "päivälle.")
    return paivadata

# Aliohjelma tilastoitavien tietojen määrittämiseen
def tilastoiTiedot(tuntidata):    
    # Lasketaan arvot 'TILASTO'-luokan jäsenmuuttujiin
    tilastot = TILASTO() 
    summa = 0 # Lasketaan summaa keskiarvoa varten
    hinnat = [] # Tähän listaan sähkön hinnat jokaiselta tunnilta

    # Hintojen lukumäärä saadaan tuntidatan olioiden lukumäärästä
    tilastot.lukumaara = len(tuntidata)
    for tunnit in tuntidata: # Lisätään 'hinnat'-listaan tuntikohtaiset hinnat desimaalilukuina
        hinnat.append(float(tunnit.hinta))
        summa += 1 

    tilastot.kallein = max(hinnat)
    tilastot.halvin = min(hinnat)
    # Etsitään vielä ajankohdat, jolloin sähkön hinta oli kalleinta ja halvinta
    lista = [] # Luodaan apulista siltä varalta, että useilla aikaleimoilla sähkön hinta olisi halvinta / kalleinta

    # Halvin hinta
    for tunnit in tuntidata:
        if float(tunnit.hinta) == tilastot.halvin:
            lista.append(tunnit.aika)
        else:
            continue
    # Listaan tallentuu siis joko yksi tai useampi ajankohta, valitaan aina ensimmäinen (tai ainoa)
    tilastot.halvinaika = lista[0]
    lista.clear() # Listan tyhjennys välissä

    # Kallein hinta
    for tunnit in tuntidata:
        if float(tunnit.hinta) == tilastot.kallein:
            lista.append(tunnit.aika)
        else:
            continue
    tilastot.kalleinaika = lista[0]
    
    lista.clear()
    tilastot.keskiarvo = sum(hinnat) / summa
    hinnat.clear()
    return tilastot

# Aliohjelma tulostuksen kirjoittamiselle
def kirjoitaTiedosto(tapa, tiedosto, lista, tilasto):

    # Tapaus, missä käyttäjä valitsee päivittäisen analyysin kirjoituksen eli valinnan 3
    if tapa == 1:
        try:
            open(tiedosto, "w").close() # Tiedoston tyhjennys
            kirjoitus = open(tiedosto, "a", encoding = "utf-8") # Avataan tiedosto
            kirjoitus.write("Analyysin tulokset " + str(tilasto.lukumaara) + " tunnilta ovat seuraavat:" + "\n")
            kirjoitus.write("Sähkön keskihinta oli " + str(round(tilasto.keskiarvo, 1)) + " snt/kWh." + "\n")
            kirjoitus.write("Halvimmillaan sähkö oli " + str(tilasto.halvin) + " snt/kWh, " + str(tilasto.halvinaika) + "." + "\n")
            kirjoitus.write("Kalleimmillaan sähkö oli " + str(tilasto.kallein) + " snt/kWh, " + str(tilasto.kalleinaika) + "." + "\n")
            kirjoitus.write("\n")
            kirjoitus.write("Päivittäiset keskiarvot (Pvm;snt/kWh):" + "\n")
            for paiva in lista: # Käydään oliolistaa (= päivien listaa) läpi alkio kerrallaan
                kirjoitus.write(paiva.paivamaara + ";" + str(round((paiva.kahinta), 1)) + "\n")
            kirjoitus.close()
            print("Tiedosto", ("'" + tiedosto + "'"), "kirjoitettu.")

        except Exception:
            print("Tiedoston", ("'" + tiedosto + "'"), "käsittelyssä virhe, lopetetaan.")
            sys.exit(0)

    # Tapaus, missä käyttäjä valitsee viikonpäiväanalyysin kirjoituksen eli valinnan 4
    elif tapa == 2:
        try:
            open(tiedosto, "w").close() # Tiedoston tyhjennys
            # Luodaan lista viikonpäivistä
            vkp = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]
            i = 0 # Luodaan apumuuttuja (indeksi) käymään läpi listan 'vkp' alkioita.
            kirjoitus = open(tiedosto, "a", encoding = "utf-8") # Avataan tiedosto
            kirjoitus.write("Viikonpäivä;Keskimääräinen hinta snt/kWh" + "\n")
            for alkio in lista: # Käydään viikonpäivittäisen datan sisältämä lista läpi alkio kerrallaan
                kirjoitus.write(vkp[i] + ";" + str(round(alkio, 1)) + "\n")
                i += 1 # Siirrytään seuraavaan viikonpäivään
            kirjoitus.close()
            print("Tiedosto", ("'" + tiedosto + "'"), "kirjoitettu.")
            vkp.clear()

        except Exception:
            print("Tiedoston", ("'" + tiedosto + "'"), "käsittelyssä virhe, lopetetaan.")
            sys.exit(0)

    return None

# Aliohjelma viikonpäivittäisten keskiarvojen laskemiseen
def viikonpaivat(tuntidata, lista):
    for i in range(0, 7): # Käydään arvosta 0 (= maanantai) arvoon 6 (= sunnuntai)
        summa = 0
        hinta = 0.0
        for tunti in tuntidata:
            pvm = datetime.datetime.strptime(tunti.aika, "%d.%m.%Y %H:%M") # Muutetaan alkion aika vastaamaan datetime arvoa
            if pvm.weekday() == i: # Jaotellaan alkiot sen mukaan, mikä viikonpäivä on kyseessä
                summa += 1
                hinta += float(tunti.hinta)
            else:
                continue
        i += 1 # Siirrytään seuraavaan viikonpäivään

        # Tarkistetaan erikseen, jos joltain viikonpäiviltä ei ole dataa ollenkaan
        if summa == 0:
            lista.append(0.0) # Silloin keskiarvohinnaksi jää loogisesti 0.0 snt/kWh
        else: # Muussa tapauksessa lisätään keskiarvot listaan
            lista.append(hinta / summa)
            
    return lista