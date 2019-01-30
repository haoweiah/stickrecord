# /usr/bin/env python
# coding=utf-8

import sys
import time

def view_bar(num,total):
    rate = num / total
    rate_num = int(rate*100)
    r = "\r[%s%s]" % ("$"*num, " "*(100-num))
    sys.stdout.write(r)
    sys.stdout.write(str(rate_num)+'%')
    sys.stdout.flush()

def downloading():
    print("开始下载")
    for i in range(101):
        time.sleep(0.05)
        view_bar(i, 100)
    print('\n 下载完成。。')

if __name__ == "__main__":
    downloading()
