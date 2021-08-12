prices = [100, 200, 300]

try:
    count = int(input("Enter a number :"))
    r = 10 // count
    print(prices[r])

except ValueError:
    print("Sorry! Invalid number. Please enter a valid number!")
except ZeroDivisionError:
    print("Sorry! Zero is not valid!")
except Exception as ex:
    print('Stopped program due to some error -> ', ex)

print("The End")
