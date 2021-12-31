num = int(input("Enter a number: "))
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num,"is a composite number")
            print(i,"times",num//i,"is",num)
            break
    else:
        print(num,"isn't a composite number")
else:
    print(num,"isn't a composite number")
