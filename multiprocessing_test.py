#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-13
# @Author  : Shoufu (gyming@outlook.com)
# @Version : 2.7.6

from multiprocessing import Pool, Queue
import os
import time
import random

q = Queue()
p = Pool()

def multiprocessing(func):
    def wrapper(*args, **kw):
        print 'Add %s to Apply Async' % func.__name__
        p.apply_async(func, args=args)
        print 'Add %s Successful!' % func.__name__
        return func(*args, **kw)
    return wrapper

@multiprocessing
def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))
    q.put(name)


if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()

    for i in range(20):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    print 'Start!'
    p.join()
    print 'All subprocesses done.'

    while not q.empty():
        print q.get()
