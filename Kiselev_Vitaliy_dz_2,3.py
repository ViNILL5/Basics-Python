first_lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(first_lst):
    if first_lst[i].lstrip("+-").isdigit():
        first_lst.insert(i, '"')
        i += 1
        if first_lst[i][0] in '+-':
            first_lst[i] = first_lst[i][0] + first_lst[i][1:].zfill(2)
        else:
            first_lst[i] = first_lst[i].zfill(2)
        first_lst.insert(i + 1, '"')
    i += 1
weather = ''
for i in first_lst:
    if i.isalpha():
        weather += ''.join(f'{" "}{str(i)}{" "}')
    else:
        weather += ''.join(str(i))
print(first_lst)
print()
print(weather)
