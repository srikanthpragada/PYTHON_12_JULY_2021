d = {1: 10, 3: 5, 2: 50, 4: 11, 8: 20, 6: 1}

for k, v in sorted(d.items(), key=lambda t: t[1]):
    print(k, v)
