stack = []

while True:
    print("Menu")
    print("====")
    print("1. Push")
    print("2. Pop")
    print("3. List")
    print("4. Exit\n")

    choice = input("Choice : ")

    if choice == '1':
        value = input("\nEnter value :")
        stack.append(value)
    elif choice == '2':
        if len(stack) > 0:
            print("\nValue = ", stack.pop())
        else:
            print("\nSorry! Stack is empty!")
    elif choice == '3':
        print("\nValues in Stack")
        for v in stack:
            print(v)
    else:
        break

print("Thank You!")
