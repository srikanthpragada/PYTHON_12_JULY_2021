def convert(s):
    return s.strip().upper()


names = ['c', ' Java', ' Python', 'C++', 'SQL', 'javascript']

for n in sorted(names, key=convert):
    print(n)
