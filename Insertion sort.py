list_item = input('Please input a list(separate with space):')
order = input('Max to min or min to max(type a or i):')
lists = list_item.split()
for i in range(0, len(lists)-1):
    j = i + 1
    while True:
        if order == 'i':
            if int(lists[j-1]) > int(lists[j]):
                lists[j], lists[j-1] = lists[j-1], lists[j]
            else:
                break
        elif order == 'a':
            if int(lists[j-1]) < int(lists[j]):
                lists[j], lists[j-1] = lists[j-1], lists[j]
            else:
                break
        j -= 1
        if j == 0:
            break
print(lists)
