found = []
unfounded = []

with open('新文字文件.txt', encoding='utf-8') as file:
    list_item = file.read()
lists = list_item.split('\n')
with open('新文字文件 (2).txt', encoding='utf-8') as file2:
    list_item_2 = file2.read()
lists_2 = list_item_2.split('\n')
for i in range(len(lists_2)):
    if lists_2[i].count(', India (') != 0:
        lists_2[i] = lists_2[i].replace(', India', '')
        lists_2[i] = lists_2[i].replace('Andhra Pradesh', '')
        lists_2[i] = lists_2[i].replace('Arunachal Pradesh', '')
        lists_2[i] = lists_2[i].replace('Assam', '')
        lists_2[i] = lists_2[i].replace('Bihar', '')
        lists_2[i] = lists_2[i].replace('Chhattisgarh', '')
        lists_2[i] = lists_2[i].replace('Goa', '')
        lists_2[i] = lists_2[i].replace('Gujarat', '')
        lists_2[i] = lists_2[i].replace('Haryana', '')
        lists_2[i] = lists_2[i].replace('Himachal Pradesh', '')
        lists_2[i] = lists_2[i].replace('Jharkhand', '')
        lists_2[i] = lists_2[i].replace('Karnataka', '')
        lists_2[i] = lists_2[i].replace('Kerala', '')
        lists_2[i] = lists_2[i].replace('Madhya Pradesh', '')
        lists_2[i] = lists_2[i].replace('Maharashtra', '')
        lists_2[i] = lists_2[i].replace('Manipur', '')
        lists_2[i] = lists_2[i].replace('Meghalaya', '')
        lists_2[i] = lists_2[i].replace('Mizoram', '')
        lists_2[i] = lists_2[i].replace('Nagaland', '')
        lists_2[i] = lists_2[i].replace('Odisha', '')
        lists_2[i] = lists_2[i].replace('Punjab', '')
        lists_2[i] = lists_2[i].replace('Rajasthan', '')
        lists_2[i] = lists_2[i].replace('Sikkim', '')
        lists_2[i] = lists_2[i].replace('Tamil Nadu', '')
        lists_2[i] = lists_2[i].replace('Telangana', '')
        lists_2[i] = lists_2[i].replace('Tripura', '')
        lists_2[i] = lists_2[i].replace('Uttar Pradesh', '')
        lists_2[i] = lists_2[i].replace('Uttarakhand', '')
        lists_2[i] = lists_2[i].replace('West Bengal', '')
        lists_2[i] = lists_2[i].replace('Andaman and Nicobar Islands', '')
        lists_2[i] = lists_2[i].replace('Jammu and Kashmir', '')
        lists_2[i] = lists_2[i].replace('Chandigarh', '')
        lists_2[i] = lists_2[i].replace('National Capital Territory', '')
        lists_2[i] = lists_2[i].replace('', '')
        lists_2[i] = lists_2[i].replace('(', '')
        lists_2[i] = lists_2[i].replace(')', '')
        lists_2[i] = lists_2[i].replace('1', '')
        lists_2[i] = lists_2[i].replace('2', '')
        lists_2[i] = lists_2[i].replace('3', '')
        lists_2[i] = lists_2[i].replace('4', '')
        lists_2[i] = lists_2[i].replace('5', '')
        lists_2[i] = lists_2[i].replace('6', '')
        lists_2[i] = lists_2[i].replace('7', '')
        lists_2[i] = lists_2[i].replace('8', '')
        lists_2[i] = lists_2[i].replace('9', '')
        lists_2[i] = lists_2[i].replace('0', '')
        lists_2[i] = lists_2[i].replace(',', '')
        print(lists_2[i], "is found")
        found.append(lists_2[i].replace(', India', ''))
print(found)
print(list_item_2.count(', India ('))