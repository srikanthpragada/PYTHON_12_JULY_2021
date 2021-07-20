# Count no. of uppercase letters in the given string

st = input("Enter string :")

count = 0
for c in st:
    if c.isupper():
        count += 1

print("No. of uppercase letters : ", count)
