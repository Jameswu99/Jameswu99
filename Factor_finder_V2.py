factors = []


def factor_finder(x):
    factor = 1
    while not factor > x:
        if x % factor == 0:
            factors.append(factor)
            print(factors)
        else:
            print(factor)
        factor += 1


factor_finder(int(input('Please type in a number:')))
