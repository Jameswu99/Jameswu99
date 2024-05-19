import random
import time

# list_item = input('Please input a list(separate with space):')
order = input('Max to min or min to max(type a or i):')
index = 0
lists = []
# lists = list_item.split()
for h in range(10240):
    lists.append(random.randint(1, 20000))
t0 = time.time()
for i in range(1, len(lists)):
    for j in range(0, len(lists)-1-index):
        k = len(lists)-j-2
        if order == 'a':
            if int(lists[k]) < int(lists[k+1]):
                lists[k], lists[k+1] = lists[k+1], lists[k]
        elif order == 'i':
            if int(lists[k]) > int(lists[k+1]):
                lists[k], lists[k+1] = lists[k+1], lists[k]
    index += 1
t1 = time.time()
print(lists)
print(t1-t0)
