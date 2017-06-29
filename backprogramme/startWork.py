#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from PyQt5 import QtCore, QtGui
import time
import global_variable


class start_work(QtCore.QThread):
    def __init__(self, parent=None):
        super(start_work, self).__init__(parent)

    def run(self):
        from weather import weather
        self.weather_this = weather()
        while global_variable.isStop == 0:
            self.weather_this.choose_city()
            time.sleep(global_variable.second)
