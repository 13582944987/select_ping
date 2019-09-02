# -*- coding: utf-8 -*-

import pandas as pd
import time
import que
import os
from PyQt5.QtCore import QEventLoop, QTimer

class Select(object):
    def __init__(self):
        pass
        self.bad_name_list = []

    def fai_ip(self,position):
        x = que.Que().start(que.get_ip_list(position))
        # print(x)
        return x

    def NotifyAdmin(self,position):
        lose_ip = self.fai_ip(position)
        for i in lose_ip:
            self.finddata(i,position)
        # return self.bad_name_list
        print('共{}离线'.format(len(self.bad_name_list)))
        self.writeLog(self.bad_name_list)

    def finddata(self,bad_ip,position):

        demo_df=pd.read_excel(r'{}'.format(position))

        for indexs in demo_df.index:
            for i in range(len(demo_df.loc[indexs].values)):
                if (demo_df.loc[indexs].values[i] == bad_ip):
                    bad_name = demo_df.loc[indexs].values[i+1]
                    print('{} {}'.format(bad_ip,bad_name))
                    self.cache_out()

                    self.bad_name_list.append(bad_name)
                    # self.writeLog(bad_name,bad_ip)
                    # print(self.bad_name_list)

    def writeLog(self,bad_name):
        path = os.getcwd()
        file_object = open(path+'.\log\ping.' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log', 'a')
        file_object.write('[%s] %s\n' % (self.timeFmt(), bad_name))
        file_object.close()
    def timeFmt(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    def cache_out(self):
        loop = QEventLoop()
        QTimer.singleShot(100, loop.quit)
        loop.exec_()

if __name__ == '__main__':

    # Select().NotifyAdmin()
    # print(Select.bad_name_list)
    Select().NotifyAdmin('K:\my_ping\ping.xlsx')
    # x = Select().finddata()
    # print(x)

    # print(bad_namelist)

    # print(x)