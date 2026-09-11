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
except (ValueError, TypeError, Nope) as e:
    print('Erreur : ', e)

# Mini exo

class RobertError(Exception):
    pass

def say_hello_age(prenom: str, age: int):
    # gerer erreurs + erreur presonnalisé si prenom == '???'
    if prenom == 'Robert':
        raise RobertError('Pas de Robert ici !')
    if type(prenom) != str:
        raise TypeError("Un prenom n'est pas different d'un string! ")
    if type(age) != int:
        raise TypeError('Un age est un int!')
    if age < 0:
        raise ValueError('Ton age ne peut pas être negatif!')
    
    return f'Bonjour {prenom} tu as {age} ans!'

try:
    print(say_hello_age('Robert', 26))
except (ValueError, TypeError, RobertError) as e:
    print('Erreur : ', e)
finally:
    print('Good Bye')

