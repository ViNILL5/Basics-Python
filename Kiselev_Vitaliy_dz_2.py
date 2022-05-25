#1 создать исходный список нечетных
#2 создать список с кубами
#3 создать цикл по суммированию цифр в числе-кубе
#4 создать цикл проверки целочисленного деления на 7
#5 суммируешь числа в получившемся списке

first_lst = list(range(1,1001, 2))

cube_lst = []
cube_lst_b = []
for number in first_lst[:]:
    cube = number ** 3
    cube_lst.append(cube)
#print(cube_lst)
general_summa = 0
general_summa_b = 0
for i in range(len(cube_lst)):
    summa = 0
    var = cube_lst[i]
    while var > 0:
        summa = summa + var % 10
        var = var // 10
    if summa % 7 == 0:
        general_summa += cube_lst[i]
print(general_summa)
# прибавляем к числам списка кубов +17
for number in cube_lst[:]:
    cube_b = number + 17
    cube_lst_b.append(cube_b)
for i in range(len(cube_lst_b)):
    summa_b = 0
    var_b = cube_lst_b[i]
    while var_b > 0:
        summa_b = summa_b + var_b % 10
        var_b = var_b // 10
    if summa_b % 7 == 0:
        general_summa_b += cube_lst_b[i]
print(general_summa_b)
