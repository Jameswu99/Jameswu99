list_item = input('Please input a list(separate with space):')
order = input('Max to min or min to max(type a or i):')
index = 0
extreme = 0
extreme_index = 0
lists = list_item.split()
for i in range(0, len(lists)):
    extreme = int(lists[i])
    extreme_index = 0
    for j in range(0+index, len(lists)):
        if order == 'i':
            if not extreme < int(lists[j]):
                extreme = int(lists[j])
                extreme_index = j
        elif order == 'a':
            if not extreme > int(lists[j]):
                extreme = int(lists[j])
                extreme_index = j
    lists[i], lists[extreme_index] = lists[extreme_index], lists[i]
    index += 1
print(lists)
