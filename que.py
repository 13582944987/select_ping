# -*- coding: utf-8 -*-

from threading import Thread
from queue import Queue
import pandas as pd
import os
import re

class Que(object):
    def __init__(self):
        self.num_threads=3
        self.q=Queue()
        self.sucess, self.failure = 0, 0
        self.failureIP = []
    def pingme(self,queue,sucess,failureIP):

        while True:
            ip=queue.get()
            ping = os.popen('ping {} -n 1'.format(ip)).read()
            # print(ping)
            select = re.compile(r'来自..+', re.M).findall(ping)
            queue.task_done()
            # print(3)
            if select == []:
                failureIP += [ip]
            else:
                sucess += 1
    def start(self,get_ip):
        self.ips = get_ip
        # print(4)
        for n in range(self.num_threads):
            t=Thread(target=self.pingme,args=(self.q,self.sucess,self.failureIP))
            t.setDaemon(True)
            t.start()
        # print(5)
        for ip in self.ips:
            self.q.put(ip)
        # print(6)
        self.q.join()
        # print(self.failureIP)
        return self.failureIP

def get_ip_list(position):
    df = pd.read_excel(position,usecols=[0])
    df_li = df.values.tolist()
    result = []
    # print(df_li)
    for s_li in df_li:
        result.append(s_li[0])
        # print(s_li)
    return result
if __name__ == '__main__':

    x = Que().start(get_ip_list('K:\my_ping\ping.xlsx'))
    print(x)

