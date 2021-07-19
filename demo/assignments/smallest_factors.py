# Smallest factor other than 1


num = int(input("Enter a number :"))
for i in range(2, num // 2 + 1):
    if num % i == 0:
        print(i)
        break
else:  # No factors found so print number as smallest factor
    print(num)
