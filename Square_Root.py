import sys
import time

num_input = float(input('Type in the number you want to get the root of:'))
digit_limit = int(input('How many digit of accuracy do you want?:'))
if digit_limit > 640:
    sys.set_int_max_str_digits(digit_limit + len(str(int(num_input))))
root = ''
root_int = 0
two_root = 0
minuend = 0
difference = 0
digit = 0
negative = ''
t0 = time.time()
if num_input < 0:
    num_input *= -1
    negative = '-'
digit = 0
if int(num_input) == 0:
    digit = 0
else:
    if len(str(int(num_input))) % 2 == 0:
        digit = int(len(str(int(num_input))) / 2)
    else:
        digit = int((len(str(int(num_input))) + 1) / 2)
num_2 = num_input
while num_2 != float(int(num_2)):
    num_2 *= 100
num = str(int(num_2))
digit_ = 0
while not (difference == '0' or digit_ > digit_limit):
    if len(num) == 1 or len(num) == 2:
        minuend = difference * 100 + int(num)
        num = num[2:]
    else:
        if len(num) % 2 == 0:
            minuend = difference * 100 + int(num[:-len(num) + 2])
            num = num[2:]
        else:
            minuend = difference * 100 + int(num[:-len(num) + 1])
            num = num[1:]
    for i in range(10):
        x = 9 - i
        if (two_root * 10 + x) * x < minuend:
            difference = minuend - (two_root * 10 + x) * x
            root = root + str(x)
            root_int = int(root)
            two_root = two_root * 10 + 2 * x
            break
        elif (two_root * 10 + x) * x == minuend:
            root = root + str(x)
            root_int = int(root)
            two_root = two_root * 10 + 2 * x
            if num == '':
                difference = '0'
                num = '0'
            break
    if len(num) == 0:
        num = '00'
    digit_ += 1
t1 = time.time()
if negative == '-':
    root = root + 'i'
    num_input = num_input * -1
root_back = root[digit:]
root_front = root[:digit]
if root_front == '':
    root_front = '0'
if root_back == '':
    print('The root of ' + str(num_input) + ' is ' + root_front)
else:
    root = root_front + '.' + root_back
    print('The root of ' + str(num_input) + ' is about ' + root)
print('Time spent:', t1 - t0, 's')
