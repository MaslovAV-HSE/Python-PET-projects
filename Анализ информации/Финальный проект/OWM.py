import datetime

import requests
from config import API_KEY, API_YANDEX
import json
import translators as tr
import time


'''res = requests.get(url="https://api.weather.yandex.ru/v2/forecast?lat=58.014965&lon=56.246723&lang=ru_RU",
                   headers={"X-Yandex-API-Key": API_YANDEX}).json()
with open("result.json", 'w') as file:
    json.dump(res, file)'''



def get_city(city):
    responce = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&lang=rus&appid={API_KEY}').json()
    return responce[0]['lat'], responce[0]['lon']

def get_responce(cords, days = 7):
    responce = requests.get(url=f"https://api.weather.yandex.ru/v2/forecast?lat={cords[0]}&lon={cords[1]}&lang=ru_RU&limit={days}",
                   headers={"X-Yandex-API-Key": API_YANDEX}).json()
    return responce

def get_current_weather(data:dict):
    return data['fact']['temp'], data['fact']['feels_like'],\
           tr.translate_text(data['fact']['condition'], from_language='en', to_language='ru')

def get_week_forcast(data:dict):
    result = []
    for i in range(7):
        dayly = {}
        day = data['forecasts'][i]
        dayly['date'] = day['date']
        dayly['temp'] = day['parts']['day_short']['temp']
        dayly['condition'] = tr.translate_text(day['parts']['day_short']['condition'],from_language='en', to_language='ru')
        result.append(dayly)
    return result

def get_city_utf(data:dict):
    return data['info']['tzinfo']['abbr']

print(get_responce(get_city("Пермь")))