def print_factors(x):
    print("The factors of", x, "are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i, end=", ")


num = int(input('Choose a number:'))
print(print_factors(num))
