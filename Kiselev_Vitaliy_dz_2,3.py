import requests
import json


URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


response = requests.get(URL)

dict_json = json.loads(response.text)


currency = input('Введите валюту (USD, EUR or GBP): ')
#try:
#  key = currency.upper()
#  date = response.headers['Date']
#  res = f"{dict_json['Valute'][key]['Value']} {date}"
#  print(res)
#except KeyError:
#    print(None)


def currency_rates(key):
  try:
    key = currency.upper()
    date = response.headers['Date']
#    start = dt.datetime.utcnow() + dt.timedelta(hours=3)
    res = f"Курс {key} равен {dict_json['Valute'][key]['Value']} на {date}"
    print(res)
  except KeyError:
    print(None)
#    time.sleep(2)


currency_rates(key)