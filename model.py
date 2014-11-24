# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, MySQLdb, time

def save_post(title, author, postCreated, wechat, postContent):
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

    # 判断表是否存在
    cur.execute("SHOW TABLES LIKE 'posts'")
    result = cur.fetchone()
    if not result:
        # 表不存在则创建表
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

    #一次插入多条记录
    # sqli="insert into student values(%s,%s,%s,%s)"
    # cur.executemany(sqli,[
    #     ('3','Tom','1 year 1 class','6'),
    #     ('3','Jack','2 year 1 class','7'),
    #     ('3','Yaheng','2 year 2 class','7'),
    #     ])
    #插入一条数据
    today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    cur.execute("INSERT INTO posts VALUES(NULL, %s, %s, %s, %s, %s, %s)", (title, author, wechat, postContent, postCreated, today))

    #修改查询条件的数据
    # cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

    #删除查询条件的数据
    # cur.execute("delete from student where age='9'")

    cur.close()
    conn.commit()
    conn.close()