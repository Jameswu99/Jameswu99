attitude = '要'
while attitude == '要':
    num = int(input("請輸入一個大於1的整數: "))
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "不是質數!")
                print(i, "乘", num // i, "是", num)
                break
        else:
            print(num, "是質數!")
    else:
        print(num, "不是質數!")
    attitude = input('您要選擇其他數字嗎？(要/不要): ')
