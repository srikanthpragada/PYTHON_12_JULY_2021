# Take a number on command line and display its factors
# Date : 05-AUG-2021

import sys

if len(sys.argv) < 2:
    print("Missing number. Please provide number on command line!")
    exit()

num = int(sys.argv[1])
for i in range(2, num // 2 + 1):
    if num % i == 0:
        print(i)
