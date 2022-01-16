lower = int(input("Please Enter the Minimum Value: "))
upper = int(input("Please Enter the Maximum Value: "))
print("Prime numbers between", lower, "and", upper, "are:")

for Number in range(lower, upper + 1):
    count = 0
    for i in range(2, (Number // 2 + 1)):
        if Number % i == 0:
            count = count + 1
            break

    if count == 0 and Number != 1:
        print("%d" % Number, end='\n')
