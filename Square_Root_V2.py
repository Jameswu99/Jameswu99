num_input = float(input('Type in the number you want to get the root of:'))
# digit_limit = int(input('How many digit of accuracy do you want?(needs to be less than 4300 or else python will break):'))
root = 0
two_root = 0
minuend = 0  # 被減數
difference = 0  # 差
digit = 0
negative = ''
if num_input < 0:
    negative = '-'
    num_input *= -1
if int(num_input) == 0:
    full_num_digit = 0
else:
    if len(str(num_input)) % 2 == 0:
        full_num_digit = len(str(int(num_input))) / 2
    else:
        full_num_digit = (len(str(int(num_input))) + 1) / 2
while num_input > 100:
    num_input /= 100
while num_input < 1:
    num_input *= 100
difference = num_input
while not difference == '0' and not digit > (309-num_input):
    for i in range(1, 11):
        x = 10 - i
        print('x', x)
        if not ((two_root*10+x)*x) > difference:
            difference = difference - (two_root * 10 + x) * x
            print('d', difference)
            root = root*10+x
            print('r', root)
            two_root = (two_root*10+x)+x
            print('t', two_root)
            break
    difference *= 100
    if difference == 0:
        difference = '0'
    print(difference)
    digit += 1
    print(digit)
