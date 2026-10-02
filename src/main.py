from pyscript import web, when
import random

runde_igang = False
liste = {"test": "grønn"}
feil_forsøk = 0

@when("click", "#start-spill")
def Start_runde(event):
    global runde_igang
    if not runde_igang:
        runde_igang = True
        ord = hent_ord("ordliste.csv")
        liste["ord"] = lag_ord_liste(ord)
        liste["tom"] = lag_tom_liste(ord)
        web.page["output"].innerText = skriv_ut_liste(liste["tom"]) # tom

@when("click", "#gjett-button")
def gjetting(event):
    input_text = web.page["bokstav"]
    bokstav = input_text.value
    nyliste = liste["tom"]
    for posisjon, i in enumerate(liste["ord"]):
        if i == bokstav:
            nyliste.pop(posisjon)
            nyliste.insert(posisjon, bokstav)
            liste["tom"] = nyliste
    else:
        web.page["output"].innerText = skriv_ut_liste(liste["tom"])
        if bokstav not in liste["ord"]:
            global feil_forsøk
            feil_forsøk += 1


        web.page["test"].innerText = feil_forsøk


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


#skriver ut liste med mellomrom mellom verdiene i listen
def skriv_ut_liste(liste):
    ord = ""
    for i in liste:
        ord += (f"{i} ")
    return ord

