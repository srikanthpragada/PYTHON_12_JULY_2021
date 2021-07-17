# Take a number and display its factors.
# If no factors found then display message prime number
# Date : 17-July-2021

found = False
num = int(input("Enter a number :"))
for i in range(2, num // 2 + 1):
    if num % i == 0:
        print(i)
        found = True

if not found:
    print("Prime number")
