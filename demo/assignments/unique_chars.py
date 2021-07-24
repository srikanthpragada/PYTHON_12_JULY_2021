names = ['Go', 'Python', 'Cobol', 'Fortran']

chars = set(names[0])

for n in names[1:]:
    chars.update(set(n))

print(sorted(chars))
