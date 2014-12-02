# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, MySQLdb, time


def __conn():
    conn= MySQLdb.connect(
            host='localhost',
            port = 3306,
            user='root',
            passwd='',
            db ='wechat_rss',
            use_unicode=1,
            charset="utf8"
        )
    return conn

def __close(conn, cur):
    cur.close()
    conn.commit()
    conn.close()

def save_post(title, author, post_created, wechat, post_content):
    conn = __conn();
    # 使用cursor()方法获取操作游标
    cur = conn.cursor()
    #插入一条数据
    today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    cur.execute("INSERT INTO posts VALUES(NULL, %s, %s, %s, %s, %s, %s)", (title, author, wechat, post_content, post_created, today))
    __close(conn, cur);
