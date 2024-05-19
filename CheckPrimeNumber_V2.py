factors = []


def factor_finder(x):
    factor = 1
    while not factor > x:
        if x % factor == 0:
            factors.append(factor)
        factor += 1


num = input('Please type in a number:')
factor_finder(int(num))
if len(factors) == 2:
    print(str(num), 'is a prime number!')
else:
    print(str(num), 'isn\'t a prime number !')
