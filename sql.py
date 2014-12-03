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
sys.stdout.write("链接数据库成功，确定新建 wechat_rss 数据库吗？可能会删除以前的 wechat_rss 数据库[y/n]")
yes = set(['yes','y', 'ye', ''])
no = set(['no','n'])
choice = raw_input().lower()

if choice in no:
   print "不执行"
elif choice in yes:
    # 删除老数据库
    cur.execute('DROP DATABASE IF EXISTS wechat_rss;')

    # 创建数据库
    cur.execute('CREATE DATABASE wechat_rss CHARACTER SET utf8;')
    print "新建数据库 wechat_rss 成功"

    # 使用数据库
    cur.execute('USE wechat_rss')
    print "使用数据库 wechat_rss"

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
    print "新建数据表 posts 成功"

    cur.close()
    conn.commit()
    conn.close()
    print "数据库关闭，程序执行完毕"
