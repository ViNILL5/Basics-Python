first_lst = list(range(1,101))

for num in first_lst[:]:
    if num % 10 == 1 and num != 11:
        print(num, 'процент')
    elif num % 10 == 2 and num != 12 or num % 10 == 3 and num !=13 or num % 10 == 4 and num != 14:
        print(num, 'процента')
    else:
        print(num, 'процентов')
