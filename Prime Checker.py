import random
import time
num = 1111111111111111111
index = 2
lists = [2]
Break = 0
join_list = 0
root_list = 1
list_index = 0
t0 = time.time()
if num > 1:
    while index ** 2 <= num:
        join_list = 0
        root_list = 1
        list_index = 0
        if num % lists[len(lists) - 1] == 0:
            Break = 1
            break
        index += 1
        while root_list != join_list:
            root_list = 0
            list_index = 0
            while lists[list_index] ** 2 <= index:
                root_list += 1
                list_index += 1
            for i in range(root_list):
                if index % lists[i] != 0:
                    join_list += 1
                else:
                    index += 1
                    join_list = 0
                    break
        lists.append(index)
else:
    Break = 1
t1 = time.time()
if Break == 0:
    print(num, 'is prime.\nTime required:', t1 - t0, 's')
else:
    print(num, 'isn\'t prime.\nTime required:', t1 - t0, 's')