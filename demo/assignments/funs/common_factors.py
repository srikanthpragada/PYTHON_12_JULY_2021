def factors(n1, n2):
    nums = []
    smallest = min(n1, n2)
    for n in range(2, smallest // 2 + 1):
        if n1 % n == 0 and n2 % n == 0:
            nums.append(n)

    return nums


print(factors(20, 30))
