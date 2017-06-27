#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pymysql
import urllib.request, urllib.parse, sys
import json
import datetime, time
from mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
import global_variable


class weather:
    '''
    def create_weather_table(self):
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

        # 创建数据表
        sql = """
                CREATE TABLE IF NOT EXISTS weather_today(
                cityname VARCHAR(10),
                week VARCHAR(10),
                time_num INT (20),
                time VARCHAR(20),
                now_temperature VARCHAR (10),
                weather VARCHAR(10),
                day_temperature VARCHAR (10),
                wind VARCHAR(20),
                index_cold VARCHAR(150),
                index_air VARCHAR(150),
                index_clothes VARCHAR(150),
                so2 INT(5),
                no2 INT(5),
                co INT(5),
                o3 INT(5),
                pm10 INT(5),
                pm25 INT(5)
              )
              """
        cur.execute(sql)

        cur.close()
        conn.commit()
        conn.close()
    '''

    def save_weather(self, weather_data):
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

        sql_insert_weather = "insert into weather_today(cityname,week,time_num,time,now_temperature,weather,day_temperature,wind,index_cold,index_air,index_clothes,so2,no2,co,o3,pm10,pm25) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        cur.execute(sql_insert_weather,
                    weather_data)

        cur.close()
        conn.commit()
        conn.close()

    def check_weather(self, cityname):
        host = 'http://jisutqybmf.market.alicloudapi.com'
        path = '/weather/query'
        method = 'GET'
        appcode = 'ed2a47358c084faaace89374fb938447'
        cityname = cityname.encode('utf8')
        querys = {'city': cityname}
        data = urllib.parse.urlencode(querys)
        bodys = {}
        url = host + path + '?' + data
        request = urllib.request.Request(url)
        request.add_header('Authorization', 'APPCODE ' + appcode)
        response = urllib.request.urlopen(request)
        content = response.read()
        content = content.decode('utf8')
        weather_json = json.loads(content)
        weather_data = [
            weather_json['result']['city'],
            weather_json['result']['week'],
            time.time(),
            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            weather_json['result']['temp'],
            weather_json['result']['weather'],
            weather_json['result']['templow'] + '~' + weather_json['result']['temphigh'],
            weather_json['result']['winddirect'] + '' + weather_json['result']['windpower'],
            weather_json['result']['index'][3]['iname'] + ':' + weather_json['result']['index'][3]['ivalue'] + ' ' +
            weather_json['result']['index'][3]['detail'],
            weather_json['result']['index'][5]['iname'] + ':' + weather_json['result']['index'][5]['index'] + ' ' +
            weather_json['result']['index'][5]['detail'],
            weather_json['result']['index'][6]['iname'] + ':' + weather_json['result']['index'][6]['ivalue'] + ' ' +
            weather_json['result']['index'][6]['detail'],
            weather_json['result']['aqi']['so2'],
            weather_json['result']['aqi']['no2'],
            weather_json['result']['aqi']['co'],
            weather_json['result']['aqi']['o3'],
            weather_json['result']['aqi']['pm10'],
            weather_json['result']['aqi']['pm2_5']
        ]
        return weather_data

    def choose_city(self):
        # self.create_weather_table()
        # print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), u'你好')
        citys = ['北京', '上海', '广州', '深圳', '杭州', '天津', '成都', '南京', '西安', '武汉']
        for i in range(len(citys)):
            weather_data = self.check_weather(citys[i])
            self.save_weather(weather_data)


class mywindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.buttonQuit.clicked.connect(QtCore.QCoreApplication.quit)
        self.buttonStart.clicked.connect(self.buttonStart_clicked)
        self.buttonStop.clicked.connect(self.buttonStop_clicked)
        self.buttonHour.clicked.connect(self.buttonHour_clicked)
        self.buttonDay.clicked.connect(self.buttonDay_clicked)
        self.button_10s.clicked.connect(self.button_10s_clicked)
        self.textState.setText(global_variable.stateText)

    @QtCore.pyqtSlot()
    def buttonStart_clicked(self):
        global_variable.isStop = 0
        global_variable.stateText = '已开始'
        stateText = global_variable.stateText + ' ' + 'start' + ' ' + '%s' % global_variable.second + 's'
        self.textState.setText(stateText)

        from startWork import start_work
        self.start_this = start_work()
        self.start_this.start()

    @QtCore.pyqtSlot()
    def buttonStop_clicked(self):
        # print('123')
        global_variable.stateText = 'stop'
        self.textState.setText(global_variable.stateText)
        global_variable.isStop = 1

    @QtCore.pyqtSlot()
    def buttonHour_clicked(self):
        from change_time import change_time
        # print('hourtime')
        self.change_time_this = change_time()
        self.change_time_this.hour_time()
        stateText = global_variable.stateText + ' ' + 'start' + ' ' + '%s' % global_variable.second + 's'
        self.textState.setText(stateText)

    @QtCore.pyqtSlot()
    def buttonDay_clicked(self):
        self.textState.setText(global_variable.stateText)
        from change_time import change_time
        # print('daytime')
        self.change_time_this = change_time()
        self.change_time_this.day_time()
        stateText = global_variable.stateText + ' ' + 'start' + ' ' + '%s' % global_variable.second + 's'
        self.textState.setText(stateText)

    @QtCore.pyqtSlot()
    def button_10s_clicked(self):
        self.textState.setText(global_variable.stateText)
        from change_time import change_time
        # print('10s')
        self.change_time_this = change_time()
        self.change_time_this.sec10_time()
        stateText = global_variable.stateText + ' ' + 'start' + ' ' + '%s' % global_variable.second + 's'
        self.textState.setText(stateText)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
