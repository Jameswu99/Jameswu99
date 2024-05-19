factors = []
num = int(input('Please type in a number:'))
i = 1
j = 0
while i ** 2 < num:
    j = 0
    if num % i == 0:
        num_1 = num
        factors.append(i)
        while num_1 != 0:
            num_1 -= i
            j += 1
        factors.append(j)
    i += 1
print(sorted(factors))
