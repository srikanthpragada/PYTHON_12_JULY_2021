num1 = 450
num2 = 250

small = num1 if num1 < num2 else num2

for i in range(2, small // 2 + 1):
    if num1 % i == 0 and num2 % i == 0:
        print(i)
