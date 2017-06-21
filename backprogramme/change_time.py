#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import global_variable


class change_time:
    def sleeptime(self, hour, min, sec):
        return hour * 3600 + min * 60 + sec;

    def hour_time(self):
        global_variable.second = self.sleeptime(1, 0, 0)

    def day_time(self):
        global_variable.second = self.sleeptime(24, 0, 0)

    def sec5_time(self):
        global_variable.second = self.sleeptime(0, 0, 5)
