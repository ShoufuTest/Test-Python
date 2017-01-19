#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-27
# @Author  : Shoufu
# @Version : 2.7.6

import pymongo
import random

conn = pymongo.MongoClient("127.0.0.1", 27017)
db = conn.mydb

c = db.users.find()
for o in c:
    print o