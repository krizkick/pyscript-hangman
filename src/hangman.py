"""
lag hangman
bruker får 6 feil (hode, kropp, arm 1 og arm 2, fot 1 og fot 2)
ordet skal hentes fra csv fil
"""

import random



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
    print(ord)

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
