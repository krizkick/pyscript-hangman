from pyscript import when, document
import random

runde_status = "vant"
liste = {"test": "grønn"}
feil= {"forsøk" : 0,
       "bokstav": []}

@when("click", "#start-spill")
def Start_runde(event):
    global runde_status, feil
    if runde_status == "igang":
        input_text = document.getElementById("bokstav")
        bokstav = input_text.value.lower()
        input_text.value = ""
        if bokstav == "":
            return

        liste["tom"] = oppdater_liste(liste["ord"], liste["tom"], bokstav)

        document.getElementById("output").innerText = skriv_ut_liste(liste["tom"])
        if bokstav not in liste["ord"] and bokstav not in feil["bokstav"]:
            feil["forsøk"] += 1
            feil["bokstav"].append(bokstav)
            document.getElementById("feil").innerText = skriv_ut_liste(feil["bokstav"])

        #sluttsjekk
        if liste["tom"] == liste["ord"]:
            runde_status = "vant"
            document.getElementById("start-spill").innerText = "Start runde"
        elif feil["forsøk"] >= len(DELER):
            runde_status = "tapt"
            document.getElementById("start-spill").innerText = "Start runde"



        tegn_galgemann(runde_status, feil["forsøk"])

    elif runde_status != "igang":
        #setter status
        runde_status = "igang"
        #bytter navn på knapp
        document.getElementById("start-spill").innerText = "Gjett"
        #resetter feil ordbok
        feil["forsøk"] = 0
        feil["bokstav"] = []
        #henter ord
        ord = hent_ord("ordliste.csv")
        liste["ord"] = lag_ord_liste(ord)
        liste["tom"] = lag_tom_liste(ord)
        document.getElementById("output").innerText = skriv_ut_liste(liste["tom"])
        tegn_galgemann(runde_status, feil["forsøk"])


DELER = [f"base{i}" for i in range(4, 11)]

def vis(id, synlig):
    document.getElementById(id).style.display = "inline" if synlig else "none"

def tegn_galgemann(runde_status, antall_feil=0):
    vis("happy", runde_status == "vant")
    for i, id in enumerate(DELER):
        vis(id, (runde_status == "igang" or runde_status == "tapt") and i < antall_feil)


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
        tilfeldig_ord = biter[tilfeldig_tall].strip().lower()
    return tilfeldig_ord


#skriver ut liste med mellomrom mellom verdiene i listen
def skriv_ut_liste(liste):
    ord = ""
    for i in liste:
        ord += (f"{i} ")
    return ord

#oppdaterer tom liste med bokstav
def oppdater_liste(fasitliste, tomliste, bokstav):
    for posisjon, i in enumerate(fasitliste):
        if i == bokstav:
            tomliste[posisjon] = bokstav
    return tomliste