import requests
import json


URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


response = requests.get(URL)

dict_json = json.loads(response.text)


currency = input('Введите валюту (USD, EUR or GBP): ')


def currency_rates():
  try:
    key = currency.upper()
    date = response.headers['Date']
    res = f"Курс {key} равен {dict_json['Valute'][key]['Value']} на {date}"
    print(res)
  except KeyError:
    print(None)


if __name__ == '__main__':
  import sys

  exit(currency_rates())