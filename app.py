# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'wechat_rss'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/<wechat>/feed', methods=['GET'])
def feed(wechat):
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from posts where wechat='" + wechat + "'")
    data = cursor.fetchall()

    if data is None:
        return "Username or Password is wrong"
    else:
        print data
        # return "Logged in successfully"
        return render_template('rss.xml', wechat=wechat, data=data)

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    # 打开调试模式
    app.debug = True
    app.run()