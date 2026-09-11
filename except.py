def rate(arg) :
    if arg == 0 : raise ValueError("1")
    else : raise TypeError("2")

try :
    rate(1)
except ValueError :
    print("VALUE ERR")
except TypeError as e :
    print(e)
    print(type(e))
    help(e)

