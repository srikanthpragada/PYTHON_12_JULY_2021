from datetime import *

persons = {}

with open("persons.txt", "rt") as f:
    for line in f:
        parts = line.strip().split(",")
        # Ignore line if it doesn't contain name and dob
        if len(parts) < 2:
            continue

        try:
            dob = datetime.strptime(parts[1], "%d-%m-%Y")
            #  Get timedelta and calculate years
            years = (datetime.now() - dob).days // 365
            persons[parts[0]] = years
        except:
            pass

for name, age in sorted(persons.items(), key=lambda t: t[1]):
    print(f"{name:10}  - {age}")
