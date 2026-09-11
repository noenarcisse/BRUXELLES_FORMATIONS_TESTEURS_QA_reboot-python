from echo import echo

"""
Exercice 3 — Les données sont parfois pourries
Les consignes sont dans enonce.md (section EXO 3).

Les données ci-dessous contiennent volontairement des valeurs invalides.
Ton code ne doit jamais planter dessus.
"""

# Mission 1 & 2
ages = ["25", "17", "bonjour", "32", "", "41", "19", "trente", "60", "  ", "28", "45"]

@echo
def moyenne(ages : list[str]) :
    sum = 0
    length = 0
    for a in ages :
        if a.isdigit() : 
            sum += int(a)
            length +=1
    return sum/length

moyenne(ages)

# Mission 2
@echo
def parse_ages(ages : list[str]):
    return [int(a) for a in ages if a.isdigit()]

parse_ages(ages)

# Mission 3
users = [
    {"name": "Alice",   "age": "25"},
    {"name": "Bob",     "age": "seventeen"},
    {"name": "Charlie", "age": "32"},
    {"name": "Diana"},
    {"name": "Evan",    "age": ""},
    {"name": "Fatima",  "age": "29"},
    {"name": "Gael",    "age": "15"},
    {"name": "Hana",    "age": "38"},
    {"name": "Igor",    "age": "quarante"},
    {"name": "Julia",   "age": "22"},
]

@echo
def get_valid_adults(users :  list[dict]):

    def keyExists(d : dict, k : str) :
        return d.get(k) != None

    adultsInTheRoom = []
    for u in users :

        if not keyExists(u, "age") : continue
        rawAge : str = str(u["age"])
        if not rawAge.isdigit() : continue
        validAge = int(rawAge)
        if validAge < 18 : continue
        # je check si le nom est dispo
        if not keyExists(u, "name") : continue

        adultsInTheRoom.append(u["name"])

    return adultsInTheRoom
    
get_valid_adults(users)
