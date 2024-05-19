pi = 0
for i in range(1, 1000000000):
    if i % 2:
        pi += 4 / (2 * i - 1)
    else:
        pi += -4 / (2 * i - 1)
print(pi)
