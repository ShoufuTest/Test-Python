#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-02
# @Author  : Shoufu (gyming@outlook.com)
# @Version : 2.7.6

import json
import requests

API_TOKEN = 'IQ6uMBfD.8169.upf-OLeqXWl4'
SENTIMENT_URL = 'http://api.bosonnlp.com/sentiment/analysis'

headers = {'X-Token': API_TOKEN}
s = [
    '倚楼听风雨，淡看江湖路',
    '转发微博',
    '到超市买酒杯，糊涂的店员送了一个红酒杯给我…………'
]
data = json.dumps(s)
print 'data', data
resp = requests.post(SENTIMENT_URL, headers=headers, data=data.encode('utf-8'))
print resp.text