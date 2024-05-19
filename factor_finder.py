def print_factors(x):
    print("The factors of", x, "are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)


while True:
    print_factors(int(input('Choose a number: ')))
    attitude = input('Do you want to choose another number? ')
    if attitude.lower() == 'yes':
        pass
    elif attitude.lower() == 'no':
        break
