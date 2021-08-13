total = 0
i = 1
while i <= 5:
    try:
        num = int(input("Enter a number: "))
        if num <= 0:
            continue

        total += num
        i += 1
    except:
        pass

print(total)
