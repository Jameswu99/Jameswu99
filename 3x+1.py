counter = 0
number = int(input('Please type in a number:'))
if number == 1:
    counter = 1
while number != 1:
    if (number % 2) == 0:
        number = int(number / 2)
        print(number)
        counter += 1
    elif (number % 2) != 0:
        number = number * 3 + 1
        print(number)
        counter += 1
print('The total stop time is :' + str(counter))


