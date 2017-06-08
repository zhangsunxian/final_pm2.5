#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json


class weather():
    url = "http://v.juhe.cn/weather/index"

    def check_weather(self, cityname):
        payload = {'format': '2', 'cityname': cityname, 'key': '2c5e54cc897b49d261b6e51d1e51f74a'}
        weather_content = requests.get(self.url, params=payload)
        weather_json = json.loads(weather_content.content)
        weather_data = [weather_json['result']['today']['city'],
                        weather_json['result']['today']['temperature'],
                        weather_json['result']['today']['weather'],
                        weather_json['result']['today']['dressing_index'],
                        weather_json['result']['today']['dressing_advice']
                        ]
        return weather_data
