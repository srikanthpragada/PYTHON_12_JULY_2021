
data = ["98,45,67", "56,67,78,87", "45,55,44", "34,54"]

for m in data:
    marks = m.split(",")
    total = sum(map(int, marks))
    avg = total // len(marks)
    print(avg)