def iseven(n):
    return n % 2 == 0


st = "AbcDef"

for c in filter(str.isupper, st):
    print(c)

for n in filter(iseven, [10, 11, 23, 40, 60]):
    print(n)
