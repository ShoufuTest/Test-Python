#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-02
# @Author  : Shoufu (gyming@outlook.com)
# @Version : 2.7.6

from snownlp import SnowNLP

s = SnowNLP(u'转发微博')
print s.words
print s.sentiments