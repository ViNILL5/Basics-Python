import re

email_dict = {}

def email_parse(email_address):
  try:
    name = re.findall(r'[a-zA-Z0-9_.+-]+', email_address)
    email_dict['username'] = name[0]
    email_dict['domain'] = name[1]
    print(email_dict)
  except IndexError:
    print('Неверный email-адрес')

email_parse('someone@geekbrains.ru')