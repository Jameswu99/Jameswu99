n = int(input('Enter a number:'))
t = 1
for i in range(1, n + 1):
    if n != t:
        print(3 ** t)
        t += 1
