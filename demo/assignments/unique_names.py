
names = []

for i in range(5):
    name = input("Enter name : ")
    if name not in names:
        names.append(name)


print(names)