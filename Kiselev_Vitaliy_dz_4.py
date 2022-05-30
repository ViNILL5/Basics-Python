first_lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']
# print(first_lst)
for i in range(len(first_lst)):
    name = first_lst[i].split(' ')[-1]
    name = name.lower().capitalize()
    elem = len(first_lst[i]) - 1
    while elem >= 0:
        if elem > 0 and first_lst[i][elem - 1].isspace():
            first_lst[i] = first_lst[i][:elem] + name
            print(f'Привет,{name}!')
            break
        elem -= 1

print(first_lst)
