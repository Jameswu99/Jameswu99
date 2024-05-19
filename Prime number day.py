from datetime import datetime, timedelta
import time

# Define start and end dates
start_date = datetime(1, 1, 1)
end_date = datetime(3000, 12, 31)

# Initialize an empty list
date_list = []
factor = 1
divide = 0
index = 0

t0 = time.time()
# Loop through the range of dates and append to the list
while start_date <= end_date:
    index = 0
    num_str = str(start_date)[:-9].replace('-', '')
    num = int(num_str)
    for i in range(0, len(num_str)-num_str[:-1].count('0')):
        if num_str[-1:] != '3' and num_str[-1:] != '7':
            break
        index += 1
        factor = 1
        divide = 0
        while num >= factor * factor:
            if num % factor == 0:
                divide += 1
            factor += 1
            if divide > 1:
                break
        if divide == 1:
            if len(str(num)) != 1:
                num = int(str(num)[1:])
        else:
            break
    if index == len(str(start_date)[:-9].replace('-', ''))-str(start_date)[:-9].replace('-', '')[:-1].count('0'):
        date_list.append(int(str(start_date)[:-9].replace('-', '')))
    start_date += timedelta(days=1)
t1 = time.time()
# Print the list of dates
# print(date_list)

print(date_list)
print(len(date_list))
print('Time required:', t1-t0, 's')
