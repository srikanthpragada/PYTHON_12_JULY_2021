
def print_factors_reverse(num):
    for n in range(num//2, 1, -1):
        if num % n == 0:
            print(n)


print_factors_reverse(120)