# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, MySQLdb, time


def __start():
    conn= MySQLdb.connect(
            host='localhost',
            port = 3306,
            user='root',
            passwd='',
            db ='wechat_rss',
            use_unicode=1,
            charset="utf8"
        )
    # 使用cursor()方法获取操作游标
    cur = conn.cursor()
    return (conn, cur)

def __close(conn, cur):
    cur.close()
    conn.commit()
    conn.close()

def save_post(title, author, post_created, wechat, post_content):
    (conn, cur) = __start();

    # 查询文章是否存在
    cur.execute("SELECT COUNT(id) FROM `posts` WHERE `title`=%s AND `wechat`=%s AND `post_created`=%s", (title, wechat, post_created))
    if cur.fetchone()[0]:
        print '-----《%s》文章已经存在，不保存数据库' % unicode(title).encode('utf-8')
    else:
        print '《%s》文章不存在，保存数据库' % unicode(title).encode('utf-8')
        #插入一条数据
        today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        cur.execute("INSERT INTO posts VALUES(NULL, %s, %s, %s, %s, %s, %s)", (title, author, wechat, post_content, post_created, today))

    __close(conn, cur)
