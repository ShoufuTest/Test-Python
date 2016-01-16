#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-13
# @Author  : Shoufu (gyming@outlook.com)
# @Version : 2.7.6

class People(object):
    # __slots__ = ('name', 'age')

    @property
    # <=> get_age()
    def age(self):
        return self.__age

    @age.setter
    # <=> set_age(value)
    def age(self, value):
        self.__age = value

    def __len__(self):
        return 100

    def __str__(self):
        return 'hehe'

    __repr__ = __str__


# p = People()
# p.age = 18      # peoperty
# print p.age     # age.setter
#
# print len(p)    # __len__()
# print p         # __str__()
# p               # __repr__()


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration
        return self.a


# for n in Fib():     # __iter__() and next
#     print n

class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start: L.append(a)
                a, b = b, a + b
            return a


# f = Fib2()
# print f[5]      #__getitem__()
# print f[0:8]    #__getitem__()


class Student(object):
    def __getattr__(self, item):
        if item == 'name':
            return 'Shoufu'
        if item == 'age':
            return lambda: 18
        return 'hehe'


# s = Student()
# print s.name        # __getattr__() variable exists
# print s.shajkhsjkd  # __getattr__() variable not exists
# print s.age()       # __getattr__() def exists

# s2 = Student()
# s2.hehe = 'hehehahaahah'
# print s2.hehe


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, item):
        return Chain('%s/%s' % (self._path, item))

    def __str__(self):
        return self._path


# print Chain().hehe.haha.hfsalkhsfajlfhjakhfj
