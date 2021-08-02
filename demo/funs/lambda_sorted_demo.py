names = ['c', ' Java', ' Python', 'C++', 'SQL', 'javascript']

for n in sorted(names, key=lambda s: s.strip().upper()):
    print(n)

