gv = 100     # Global variable

def outer():
    global gv
    gv = gv + 1
    print("Outer function")
    a = 10    # Enclosing variable

    # Local function
    def inner():
        nonlocal a
        a = 1
        b = 20   # Local variable
        print(gv, a, b)

    inner()
    print(a)   # ?


outer()
