def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf
def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
while True:
    num1 = int(input('選個數字:')) 
    num2 = int(input('選個數字:'))
    advt = input('你想求最小公倍數還是最大公因數?(輸入LCM或HCF):')
    if advt == 'LCM':
        print("兩數的最小公倍數是", compute_lcm(num1, num2))
    elif advt == 'HCF':
        print("兩數的最大公因數是", compute_hcf(num1, num2))
    dvt = input('你想要再來一次嗎?(輸入yes或no):')
    if dvt.lower() == 'no':
        break
