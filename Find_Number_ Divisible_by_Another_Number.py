num = input('May I ask which multiple of the number you want to find: ') 
users_wish = False
my_list = []
while users_wish == False:
    users_wishes = input('Choose a number: ')
    my_list.append(input('Do you want to choose a number ? '))
    if users_wishes == 'no':
        break
result = list(filter(lambda x: (x % int(num) == 0), my_list))
print("Numbers divisible by", num, "are",result)
