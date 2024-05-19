def prime_factoring(n):
    divisor = 2
    factors = []
    while divisor * divisor <= n:
        if n % divisor:
            divisor += 1
        else:
            n //= divisor
            factors.append(divisor)

    if n > 1:
        factors.append(n)

    return factors


aNumber = int(input("Enter a number:"))

print(prime_factoring(aNumber))
