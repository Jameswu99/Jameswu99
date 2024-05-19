num_low = int(input('Type in lower number to determine the range:'))
num_high = int(input('Type in higher number to determine the range:'))
x = 1
x_2 = 0


for index in range(num_low, num_high+1):
    while not x*x > index:
        if index % x == 0:
            if x == int(index/x):
                x_2 += x
            else:
                x_2 += x + int(index/x)
        x += 1
        if x_2 > 2*index:
            break
    if x_2 == 2*index:
        print(index)
    x_2 = 0
    x = 1
