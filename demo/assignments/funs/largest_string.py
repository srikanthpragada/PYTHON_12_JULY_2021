def largest(*names):
    bigstr = names[0]
    for n in names[1:]:
        if len(n) > len(bigstr):
            bigstr = n

    return bigstr


l = largest('Python', 'JavaScript', 'Java')
print(l)
