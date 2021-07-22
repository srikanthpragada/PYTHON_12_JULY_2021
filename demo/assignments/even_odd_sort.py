# Sort even and odd numbers and print them 

evens = []
odds = []

while True:
    num = int(input("Enter a number :"))
    if num == 0:
        break

    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

for n in sorted(evens) + sorted(odds):
    print(n)