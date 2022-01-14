announced_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(announced_list))
'''
message = ''
for i in announced_list:
    message += i
    message += ' '
    print(type(i))
print (message)
'''

announced_list =announced_list[::-1]

for i in announced_list:
    if announced_list[announced_list.index(i)].isdigit() == True and announced_list[announced_list.index(i)].startswith('"') == False:
        announced_list.insert(announced_list.index(i) + 1, '"')
    elif announced_list[announced_list.index(i)].isdigit() == False and announced_list[announced_list.index(i)].startswith('+') == True:
        announced_list.insert(announced_list.index(i) + 1, '"')

announced_list =announced_list[::-1]

for i in announced_list:
    if announced_list[announced_list.index(i)].isdigit() == True and announced_list[announced_list.index(i)].startswith('"') == False:
        announced_list.insert(announced_list.index(i) + 1, '"')
        if len(i) == 1:
            announced_list[announced_list.index(i)] = '0'+ i

    elif announced_list[announced_list.index(i)].isdigit() == False and announced_list[announced_list.index(i)].startswith('+') == True:
        announced_list.insert(announced_list.index(i) + 1, '"')


message= ' '.join(announced_list)
print(message)