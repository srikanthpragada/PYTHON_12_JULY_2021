data = ["1,Steve", "5,Joe", "4,Adams", "3,Larry", "11,Bill", "12-Bob"]

students = {}

for entry in data:
    if ',' not in entry:
        continue

    rollno, name = entry.split(",")
    students[int(rollno)] = name

for k, v in sorted(students.items()):
    print(f"{k:3} {v}")
