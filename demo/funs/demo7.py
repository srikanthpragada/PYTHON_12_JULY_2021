# Variable arguments

def wish(*names, message="Hi"):
    for n in names:
        print(f"{message} {n}", end=' ')


wish("Anders", "Larry", message="Hello")
wish("Li", "Ji", "Fi")
