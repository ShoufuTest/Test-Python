#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-16
# @Author  : Shoufu (gyming@outlook.com)
# @Version : 2.7.6
# @Function:
#   注意到consumer函数是一个generator（生成器），把一个consumer传入produce后：
#       首先调用c.next()启动生成器；
#       然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
#       consumer通过yield拿到消息，处理，又通过yield把结果传回；
#       produce拿到consumer处理的结果，继续生产下一条消息；
#       produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

import time


def consumer():
    r = ''
    while True:
        n = yield r  # 把consumer函数变成一个generator（生成器）
        if not n:
            return
        print '[CONSUMER] Consuming %s ...' % n
        time.sleep(1)
        r = '200 ok'


def produce(c):
    c.next()  # 调用c.next()启动生成器
    n = 0
    while n < 5:
        n += 1
        print '[PRODECER] Producing %s ...' % n
        r = c.send(n)  # 一旦生产了东西，通过c.send(n)切换到consumer执行
        print '[PRODECER] Consumer return: %s' % r
    c.close()


c = consumer()
produce(c)
