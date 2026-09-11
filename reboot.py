username = "Sofian"
age = 25
price = 99.99
boolean = True
is_adult = age >= 18

lst = [1, 2, 3]
tup = (1, 2, 3)
ensemble = {1, 2, 3, 4, 5}
dico = {
    "formation_name": "QA Testeurs",
    "nb_stagiaire": 12,
    "technos_used": ["Python", "Jira", "JavaScript"],
    "adresse": {
        "rue": "Rue Jules Cockx",
        "post_code": 1160
    }
}


lst_avec_doublons = [1, 1, 1, 5, 5, 7, 7, 7, 8, 8, 4, 4]
lst_sans_doublons = list(set(lst_avec_doublons))

premier_element_tab = lst[0]

formation_name_pas_safe = dico["formation_name"]
formation_name_safe = dico.get("formation_name")
print(formation_name_safe)

longueur = len(lst)

lst_technos = ["Python", "JavaScript", "C#", "Rust", "TypeScript", "C++", "PhP"]

for techno in lst_technos:
    # match techno:
    #     case "PhP":
    #         print('aaargh')
    #     case "Python":
    #         print('Banger')
    #     case _:
    #         print("C'est bien")

    
    if techno == "PhP":
        print('aaargh', techno)
    elif techno == "Python":
        print('Banger', techno)
    elif techno == "Rust":
        pass
    else:
        print("C'est bien", techno)

for i in range(10):
    print(i)

for i in range(len(lst_technos)):
    print(lst_technos[i])

start = 0
stop = 15
step = 1

for i in range(start, stop, step):
    print(i)

for index, element in enumerate(lst_technos):
    print(f'elem = {element} --- index = {index}')
    if element == "Python":
        continue
    print('Sans le continue hehe')


iteration = 0

while iteration < 10:
    if iteration == 5:
        break
    print(f'Iteration {iteration}')
    # iteration = iteration + 1
    iteration += 1

game = True
nb = int(input("Donne un nombre"))

while game and nb % 2 == 0:
    reponse = input("Voulez vous continuer à jouer ? (o/n)")
    if reponse == "o":
        continue
    else:
        game = False

# result = ""
# if game:
#     result = "Je joue"
# else:
#     result = "Je joue pas"

result = "Je joue" if game else "Je joue pas"

test = 2

result2 = "zero" if test == 0 else "1" if test == 1 else 'deux'

grand_tab = [i for i in range(100)]
grand_tab_pair = [i for i in range(100) if i % 2 == 0]
grand_tab_de_carre = [i**2 for i in range(100)]
print(grand_tab)
print(grand_tab_pair)
print(grand_tab_de_carre)

lst_sans_php = [techno.upper() for techno in lst_technos if techno != "PhP"]
print(lst_sans_php)
