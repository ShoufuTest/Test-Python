#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-02-06
# @Author  : Shoufu (gyming@outlook.com)
# @Version : 2.7.6

from multiprocessing.managers import BaseManager
import random
import Queue


class QueueManager(BaseManager):
    pass


url_queue = Queue.Queue()
json_queue = Queue.Queue()
flag_queue = Queue.Queue()

flag_queue.put(1)

for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    url_queue.put(n)

QueueManager.register('get_url_queue', callable=lambda: url_queue)
QueueManager.register('get_json_queue', callable=lambda: json_queue)
QueueManager.register('get_flag_queue', callable=lambda: flag_queue)

manager = QueueManager(address=('', 5000), authkey='heheda')
manager.start()

result = manager.get_json_queue()

while True:
    print 'Result:', result.get()

manager.shutdown()
