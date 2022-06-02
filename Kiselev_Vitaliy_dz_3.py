from collections import defaultdict

names_lst = ['Миша', 'Паша', 'Поля', 'Маша', 'Оля']

def thesaurus():
    key_lst = []
    for name in names_lst[:]:
        letter = name[0]
        key_lst.append(letter)
      
    names = defaultdict(list)
    for key, value in zip(key_lst, names_lst):
        names[key].append(value)
    print(dict(names))

  
thesaurus()