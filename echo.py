def echo(f) :
    def myinner(*args, **kwargs):
        # print(f"{f.__name__}({args}) \n {f(*args, **kwargs)}")
        print(f.__name__)
        print(f(*args, **kwargs))
        print("------")
    return myinner