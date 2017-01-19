#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-13
# @Author  : Shoufu
# @Version : 2.7.6

import re
import json
import requests


def fetch(pageCode):
    sg_data = re.findall('window.sg_data=([\\s\\S]*)seajs.use', pageCode)[0]
    src = re.findall('src:"(.*?)"', sg_data)[0]
    ver = re.findall('ver:"(.*?)"', sg_data)[0]
    timestamp = re.findall('timestamp:"(.*?)"', sg_data)[0]
    signature = re.findall('signature:"(.*?)"', sg_data)[0]

    return {
        'src': src,
        'ver': ver,
        'timestamp': timestamp,
        'signature': signature
    }


def wechat_get_num(url):
    r = requests.get(url)
    sg_data = fetch(r.text)
    comment_url = 'http://mp.weixin.qq.com/mp/getcomment?src={0}&ver={1}&timestamp={2}&signature={3}'.format(
        sg_data['src'], sg_data['ver'], sg_data['timestamp'], sg_data['signature'])
    data_str = requests.get(comment_url).text
    return json.loads(data_str)

url = 'https://mp.weixin.qq.com/s?src=3&timestamp=1463129219&ver=1&signature=yBxBj89A3-xNyI5SVomzQK323M6VIMf1d98P01Swi*0Gw-c0am8NFYTD6YXDfcYGkMXf-nYtU-BxqDIRDCxn7TgpVRn-s2otG09i5McrMSTyK785mql4wpQ5dybixQOjd91tqFKA0YVQq3MhYqO*MSfr9ui54-0KVqxUkFRR3zU='
data = wechat_get_num(url)
print '文章的阅读数：', data['read_num']
print '文章的点赞数：', data['like_num']

