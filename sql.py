# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 数据库初始化
import sys, MySQLdb

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='',
        use_unicode=1,
        charset="utf8"
    )
# 使用cursor()方法获取操作游标
cur = conn.cursor()
# 创建数据库
cur.execute('create database wechat_rss')
# 使用数据库
cur.execute('use wechat_rss')
# 创建表
cur.execute("""
    CREATE TABLE IF NOT EXISTS `posts` (
        `id` INT(11) NOT NULL AUTO_INCREMENT,
        `title` VARCHAR(200),
        `author` VARCHAR(50),
        `wechat` VARCHAR(50),
        `content` TEXT,
        `post_created` DATE,
        `created` DATE,
        PRIMARY KEY (`id`)
    )
    """)

cur.close()
conn.commit()
conn.close()
