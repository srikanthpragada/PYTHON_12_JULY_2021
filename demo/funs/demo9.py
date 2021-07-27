# Return value

def even(num):
    return num % 2 == 0


def hasupper(st):
    for c in st:
        if c.isupper():
            return True

    return False


def next_even(num):
    if num % 2 == 0:
        return num + 2
    else:
        return num + 1


print(even(10))
print(hasupper("abc"))
