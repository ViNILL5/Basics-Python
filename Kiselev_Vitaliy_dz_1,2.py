dictionary = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv():
    result = dictionary.get(num.lower(), None)
    if num[0].isupper():
        print('Перевод: ', result.capitalize())
    else:
        print('Перевод: ', result)


while True:
    num = input('Напишите цифру от 0 до 10 на английском: ')
    num_translate_adv()