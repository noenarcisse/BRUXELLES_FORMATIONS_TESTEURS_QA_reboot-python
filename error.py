# value = int(input('Donne un nombre : '))
# print(value)

dico = {
    "name": "Noé",
    "Tech": 'Go'
}

# print(dico["nam"]) => Erreur

name = dico["name"]

# print(name / 5)

def maj(prenom: str) -> str:
    return prenom.upper()

print(maj('Kenny'))

class Nope(Exception):
    pass

def div(a: int, b: int):
    try:
        print(a / b)
        print('La division a bien eu lieu!')
    except ZeroDivisionError:
        print('Echoué! Tu peux pas diviser par zero!')
    except TypeError:
        print("Diviser par un string? t'es trop nul!")
    finally:
        print('Fin du programme')

def div2(a: int, b: int):
    if a == 5:
        raise Nope('NOPE')
    if b == 0:
        raise ValueError("Le diviseur ne peut pas être zero!")
    if type(a) != int or type(b) != int:
        raise TypeError("Les paramètres doivent être des entiers!")
    return a, b



# div(5, 'hello')



try:
    print(div2(5, 'Hello'))
except (ValueError, TypeError) as e:
    print('Erreur : ', e)

