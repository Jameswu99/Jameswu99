num = int(input("請輸入一個大於1的整數: "))
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num,"是合數!")
            print(i,"乘",num//i,"是",num)
            break
    else:
        print(num,"不是合數!")
else:
    print(num,"不是合數!")
