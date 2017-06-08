#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb


class create_weather():
    def create_weather_table(self):
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            db='weather'
        )
        cur = conn.cursor()

        # 创建数据表
        sql = """CREATE TABLE IF NOT EXISTS weather_today(
              cityname VARCHAR(20),
              temperature VARCHAR (20),
              weather VARCHAR(30),
              dressing_index VARCHAR (10),
              suggestions VARCHAR(100)
              )"""
        cur.execute(sql)

        cur.close()
        conn.commit()
        conn.close()
