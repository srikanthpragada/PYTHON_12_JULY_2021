s1 = "TypeScript"
s2 = "JavaScript"

for c in sorted(set(s1)):
    if c in s2:
        print(c)