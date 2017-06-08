#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb


class save_to_mysql():
    def save_weather(self, weather_data):
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            db='weather'
        )
        cur = conn.cursor()

        sql_insert_weather = "insert into weather_today(cityname,temperature,weather,dressing_index,suggestions) values(%s,%s,%s,%s,%s)"

        cur.execute(sql_insert_weather,
                    weather_data)

        cur.close()
        conn.commit()
        conn.close()
