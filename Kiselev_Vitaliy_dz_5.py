first_lst = [5.5, 10.1, 20.35, 36, 48.15, 15.03, 12, 7, 18.8, 6]
#1
price = []
cost = 0
for i in range(len(first_lst)):
    rub = int(first_lst[i])
    kop = round(100 * (first_lst[i] % 1))
    cost = f'{rub} руб {kop:02} коп'
    price.append(cost)
print(', '.join(price))
#2
print()
print(first_lst)
print(id(first_lst))

first_lst.sort()
print(id(first_lst))
print(first_lst)
#3
print()
revers_first_lst = sorted(first_lst, reverse=True)
print(revers_first_lst)
#4
print()
print(first_lst[-5:])
