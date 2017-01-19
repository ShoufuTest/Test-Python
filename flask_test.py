#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-16
# @Author  : Shoufu (gyming@outlook.com)
# @Version : 2.7.6
# @Function:
#   写一个app.py，处理3个URL，分别是：
#   GET /：首页，返回Home；
#   GET /signin：登录页，显示登录表单；
#   POST/signin：处理登录表单，显示登录结果。

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/<name>', methods=['GET', 'POST'])
def hello(name):
    return '<h1>Hello, %s!</h1>' % name

from flask import render_template

@app.route('/signin', methods=['GET'])
def signif_form():
    return render_template('form.html',username='hehe')

@app.route('/signin', methods=['POST'])
def signin():
    print request.form
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

# Default route, print user's IP
@app.route('/ip')
def index():
    ip = request.remote_addr
    return render_template('index.html', user_ip=ip)

app.run(debug=True)