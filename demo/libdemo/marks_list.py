# Print name and marks
f = open("marks.txt", "rt")
for line in f:
    line = line.strip()
    if len(line) == 0:  # Blank line
        continue

    name, *marks = line.split(",")
    if len(marks) == 0:
        continue

    marks = filter(str.isdigit, marks)  # Take only numbers
    total = sum(map(int, marks))        # Convert str to it and sum it
    print(f"{name:15} {total:4}")

f.close()
