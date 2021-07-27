# Keyword arguments

def fun(**args):
    print(args)


def details(*args, **kwargs):
    pass


fun(a=10, b=20)
fun(name="Joe", email='joe@gmail.com')
details(10, 20, a=100)
