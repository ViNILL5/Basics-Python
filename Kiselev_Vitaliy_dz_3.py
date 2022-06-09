from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена', 'Полина', 'Кристина', 'Мария'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


gen_pupils_lst = ((t, k) for t, k in zip_longest(tutors, klasses))


print(type(gen_pupils_lst))
print()

while True:
  print(next(gen_pupils_lst))