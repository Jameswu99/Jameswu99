import math;

def eratosthenes(n):
    P = [i for i in range(2, (int)(math.sqrt(n)+1))]
    p = 0
    while True:
        for i in P[p + 1:]:
            if i % P[p] == 0:
                P.remove(i)
        if P[p]**2 >= P[-1]:
            break
        p += 1
    return P

aNumber = (int)(input("Enter a number:"));
factors = eratosthenes(aNumber);

num = aNumber;

for divisor in factors:
        while( num % divisor == 0 ):
            num //= divisor
            print(divisor, ' ', end = '');
