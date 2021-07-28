def process(value, func):
    result = func(value)  # len(value)
    print(result)


process('abc', len)  # Pass fun as parameter
process(-10, abs)
