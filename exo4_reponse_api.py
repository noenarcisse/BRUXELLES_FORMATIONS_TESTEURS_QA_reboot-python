from echo import echo
"""
Exercice 4 — Vous avez reçu une réponse API
Les consignes sont dans enonce.md (section EXO 4).

`response` imite ce qu'une API comme EventFlow pourrait renvoyer.
Aucun appel réseau ici : c'est un simple dictionnaire Python.
"""

response = {
    "status": 200,
    "data": [
        {"id": 1,  "title": "Metal Night",           "capacity": 300,  "active": True},
        {"id": 2,  "title": "Python Conference",      "capacity": 150,  "active": False},
        {"id": 3,  "title": "Rock Festival",          "capacity": 500,  "active": True},
        {"id": 4,  "title": "Techno Warehouse",       "capacity": 800,  "active": True},
        {"id": 5,  "title": "Jazz & Blues Evening",   "capacity": 120,  "active": True},
        {"id": 6,  "title": "Indie Showcase",         "capacity": 90,   "active": False},
        {"id": 7,  "title": "Hip-Hop Block Party",    "capacity": 650,  "active": True},
        {"id": 8,  "title": "Classical Gala",         "capacity": 400,  "active": False},
        {"id": 9,  "title": "Electro Sunset",         "capacity": 1000, "active": True},
        {"id": 10, "title": "Folk Acoustic Session",  "capacity": 60,   "active": True},
        {"id": 11, "title": "Reggae Beach Party",     "capacity": 750,  "active": True},
        {"id": 12, "title": "Drum & Bass Marathon",   "capacity": 900,  "active": False},
    ],
}


# Q1 — Afficher le status.
def LogStatus(res : dict) :
    print(res["status"])

LogStatus(response)
# Q2 — Afficher tous les titres.
def PrintTitles(res) :
    body = res["data"]
    for e in body : print(e["title"])
PrintTitles(response)
# Q3 — Afficher uniquement les événements actifs.
def PrintActiveEvents(res) :
    body = res["data"]
    for e in body : 
        if e["active"] : print(e) 
PrintActiveEvents(response)

# Q4 — Compter les événements actifs.
# fallait plutot
# actives = [e for e in body if e.get("active")]

@echo
def countActiveEvent(res : dict) :
    body : list[dict] = res["data"]
    f = lambda e : e["active"] == True
    actives = filter(f, body)
    return len(list(actives))

countActiveEvent(response)

# Q5 — Trouver l'événement ayant la plus grande capacité.
@echo
def findBiggestCapacity(res) :
    return max(res["data"], key= lambda e : e["capacity"])

findBiggestCapacity(response)

# Q6
def find_event(response, event_id):
    body : list[dict] = response["data"]
    return next((e for e in body if e.get("id") == event_id), None)

find_event(response,2)
find_event(response,13)

# Q7 — Vérification manuelle : afficher PASS si le status vaut 200, sinon FAIL.
@echo
def displayStatusMessage(response, event_id):
    if response["status"] == 200 : return "PASS"
    return "FAIL"