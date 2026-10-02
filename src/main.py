from pyscript import web, when
import random

runde_igang = False
liste = {}

@when("click", "#gjett-button")
def gjetting(event):
    if not runde_igang:
        input_text = web.page["bokstav"]
        bokstav = input_text.value
        feil_gjett = 0
        while feil_gjett < 6 and runde_igang:
            web.page["output"].innerText = skriv_ut_liste(liste["ord"])
            plassering = 0
            print(liste["ord"])
            for i in liste["ord"]:
                if i == bokstav:
                    nyliste = liste["tom"]
                    nyliste.pop(plassering)
                    nyliste.insert(plassering, i)
                plassering += 1
            else:
                if bokstav not in nyliste:
                    feil_gjett += 1
"""


    
        plassering = 0
        for i in ord_i_liste:
            if i == gjett:
                status.pop(plassering)
                status.insert(plassering, i)
            plassering += 1
        else:
            if gjett not in status:
                feil_gjett += 1
    else:
        skriv_ut_liste(status)
        print("ordet var:")
        skriv_ut_liste(ord_i_liste)
    return runde_over(status)



"""
@when("click", "#start-spill")
def Start_runde(event):
    global runde_igang
    if not runde_igang:
        runde_igang = True
        ord = hent_ord("ordliste.csv")
        liste["ord"] = lag_ord_liste(ord)
        liste["tom"] = lag_tom_liste(ord)
        web.page["output"].innerText = skriv_ut_liste(liste["tom"])



"""
#while løkke holder spillet igang til bruker taper
spill_i_gang = True
poeng = 0
while spill_i_gang:
    ord = hent_ord("ordliste.csv")
    spill_i_gang = spill_runde(ord)
    if spill_i_gang:
        poeng += 1
else:
    print(f"du fikk {poeng} poeng!")
"""
"""
lag hangman
bruker får 6 feil (hode, kropp, arm 1 og arm 2, fot 1 og fot 2)
ordet skal hentes fra csv fil
"""

def lag_ord_liste(ord):
    ord_i_liste = []
    for bokstav in ord:
        ord_i_liste.append(bokstav)
    return ord_i_liste

def lag_tom_liste(ord):
    status = []
    for bokstav in ord:
        status.append("_")
    return status



#henter tilfeldig ord fra fil
def hent_ord(csv):
    with open(csv, "r") as fil:
        tekst = fil.read()
        biter = tekst.split(",")
        tilfeldig_tall = random.randint(0, (len(biter)-1))
        tilfeldig_ord = biter[tilfeldig_tall]
    return tilfeldig_ord

#returnerer true om runden er over
def runde_over(liste):
    return not "_" in liste

#skriver ut liste med mellomrom mellom verdiene i listen
def skriv_ut_liste(liste):
    ord = ""
    for i in liste:
        ord += (f"{i} ")
    return ord

#en runde i spillet, gi inn et ord, returnerer True vis bruker vinner 
def spill_runde(ord):
    ord_i_liste = []
    status = []
    for bokstav in ord:
        ord_i_liste.append(bokstav)
        status.append("_")
    feil_gjett = 0
    while feil_gjett < 6 and not runde_over(status):
        skriv_ut_liste(status)
        gjett = input("bokstav:\n")
        plassering = 0
        for i in ord_i_liste:
            if i == gjett:
                status.pop(plassering)
                status.insert(plassering, i)
            plassering += 1
        else:
            if gjett not in status:
                feil_gjett += 1
    else:
        skriv_ut_liste(status)
        print("ordet var:")
        skriv_ut_liste(ord_i_liste)
    return runde_over(status)
