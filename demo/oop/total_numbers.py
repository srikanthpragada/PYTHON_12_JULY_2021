total = 0
for i in range(5):
    try :
        num = int(input("Enter a number: "))
        total += num
    except:
        pass

print(total)
