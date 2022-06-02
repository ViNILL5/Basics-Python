from random import choice, sample

"Даны три списка, из них рандомно выбирается по слову"

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

number = int(input('Введите количество повторов: '))


def get_jokes(number):
  for i in range(number):
    word_nouns = choice(nouns)
    word_adverbs = choice(adverbs)
    word_adjectives = choice(adjectives)
    joke = [f'{word_nouns} {word_adverbs} {word_adjectives}']
    print(joke)
#    if number > 1:
#      print(joke.sample)


get_jokes(number)