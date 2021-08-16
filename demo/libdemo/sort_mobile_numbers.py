# Write all valid mobile numbers from mobile.txt to valid_mobiles.txt

with open("mobiles.txt", "rt") as f:
    mobiles = set()
    for line in f:
        entries = line.split(",")
        for e in entries:
            e = e.strip()
            if len(e) == 10 and e.isdigit():
                mobiles.add(e)

with open("valid_mobiles.txt","wt") as f:
    for mobile in sorted(mobiles):
        f.write(mobile + "\n")



