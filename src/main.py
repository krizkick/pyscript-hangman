from pyscript import when, document
import random

runde_igang = False
liste = {"test": "grønn"}
feil_forsøk = 0

@when("click", "#start-spill")
def Start_runde(event):
    global runde_igang, feil_forsøk
    if not runde_igang:
        runde_igang = True
        feil_forsøk = 0
        ord = hent_ord("ordliste.csv")
        liste["ord"] = lag_ord_liste(ord)
        liste["tom"] = lag_tom_liste(ord)
        document.getElementById("output").innerText = skriv_ut_liste(liste["tom"])
        tegn_galgemann(runde_igang, feil_forsøk)

@when("click", "#gjett-button")
def gjetting(event):
    global feil_forsøk, runde_igang
    if not runde_igang:
        return
    input_text = document.getElementById("bokstav")
    bokstav = input_text.value.lower()
    input_text.value = ""
    if bokstav == "":
        return

    for posisjon, i in enumerate(liste["ord"]):
        if i == bokstav:
            liste["tom"][posisjon] = bokstav

    document.getElementById("output").innerText = skriv_ut_liste(liste["tom"])
    if bokstav not in liste["ord"]:
        feil_forsøk += 1

    if feil_forsøk >= len(DELER) or liste["tom"] == liste["ord"]:
        runde_igang = False

    tegn_galgemann(runde_igang, feil_forsøk)


DELER = [f"base{i}" for i in range(5, 11)]

def vis(id, synlig):
    document.getElementById(id).style.display = "inline" if synlig else "none"

def tegn_galgemann(spill_igang, antall_feil=0):
    vis("happy", not spill_igang)
    for i, id in enumerate(DELER):
        vis(id, spill_igang and i < antall_feil)

tegn_galgemann(False)   # start: glad gutt

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

