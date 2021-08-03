def hasupper(st):
    for c in st:
        if c.isupper():
            return True

    return False


names = ['abc', 'Abc', 'PQR', 'xyz', 'pQr', 'Bbc']

for s in filter(hasupper, names):
    print(s)

for s in filter(lambda s: s[0].isupper() and s[1:].islower(), names):
    print(s)
