#!/usr/bin/env python3
# coding=utf-8
from flask import Flask, request, render_template, jsonify, json
import pymysql
from datapredict import datapredict

app = Flask(__name__)


@app.route('/scan/<city_name>', methods=['GET'])
def scan(city_name):
    conn = pymysql.connect(
        host='rm-uf61zu38p9t1h913mo.mysql.rds.aliyuncs.com',
        port=3306,
        user='root',
        passwd='hzw123456+-',
        db='weather',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    cur = conn.cursor()
    # sql = "select * from weather_today WHERE cityname ='%s',(select max(time_num) from weather_today)-10<=time_num" % (city_name)
    sql = "select * from weather_today WHERE time_num>=(select max(time_num) from weather_today)-10 and cityname ='%s'" % (
        city_name)
    cur.execute(sql)
    results = cur.fetchall()
    pm25data = [
        results[0]['so2'],
        results[0]['no2'],
        results[0]['co'],
        results[0]['o3']
    ]
    # for row in results:
    pm25predict=datapredict()
    json_result = {'cityname': results[0]['cityname'], 'week': results[0]['week'],
                   'now_temperature': results[0]['now_temperature'],
                   'day_temperature': results[0]['day_temperature'],
                   'weather': results[0]['weather'], 'index_cold': results[0]['index_cold'],
                   'index_air': results[0]['index_air'], 'index_clothes': results[0]['index_clothes'],
                   'pm25': results[0]['pm25'], 'pm25pre': str(pm25predict.predict(pm25data))}
    cur.close()
    conn.commit()
    conn.close()
    return json.dumps(json_result, ensure_ascii=False)


@app.route('/')
def index():
    return render_template('new.html')


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=8080,
        debug=True
    )
