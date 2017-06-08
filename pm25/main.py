#!/usr/bin/python
# -*- coding: UTF-8 -*-
import weather_from_internet
import save_to_mysql
import create_weather

if __name__ == '__main__':
    test = weather_from_internet.weather()
    save = save_to_mysql.save_to_mysql()
    create = create_weather.create_weather()
    create.create_weather_table()
    citys = ['北京']
    # citys = ['北京', '上海', '广州', '深圳', '杭州', '天津', '成都', '南京', '西安', '武汉']
    for i in range(len(citys)):
        weather_data = test.check_weather(citys[i])
        save.save_weather(weather_data)
