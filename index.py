# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, urllib2, re, json, MySQLdb, time

# type 1是标题 2是文章内容 3是总页数
def getHtml(url, type):
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(url, headers=headers)
    content = urllib2.urlopen(req).read()   # UTF-8

    if type == 1:
        title = re.compile('<a class="question_link" href="(.*)" .* target="_blank">\\n*(.*)\\n*</a>')
    elif type == 2:
        title = re.compile('<div class="rich_media_content" id="js_content">\\n*(.*)\\n*</div>')
    elif type == 3:
        title = re.compile('<strong>...</strong>\\n*&nbsp;\\n*<a href=".*">(.*)</a>')
    return re.findall(title, content)

def savePost(title, wechat, content):
    conn= MySQLdb.connect(
            host='localhost',
            port = 3306,
            user='root',
            passwd='',
            db ='test',
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
                `id` INT(11),
                `title` VARCHAR(50),
                `author` VARCHAR(50),
                `wechat` VARCHAR(10),
                `content` TEXT,
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
    cur.execute("INSERT INTO posts VALUES('', %s, '深度阅读', %s, %s, %s)",(
        title, wechat, content, today))

    #修改查询条件的数据
    # cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

    #删除查询条件的数据
    # cur.execute("delete from student where age='9'")

    cur.close()
    conn.commit()
    conn.close()

wechat = 'givemesomefood'
# 获取总页数
url = "http://chuansongme.com/account/%s?start=%d"
u = url % (wechat, 0)
page = getHtml(u, 3)

# for p in xrange(0, int(page[0])+1):
for p in xrange(0, 1):
    # 获取标题
    u = url % (wechat, 0*12)
    page = getHtml(u, 1)
    if p<12:
        # 获取内容
        contentUrl = "http://chuansongme.com" + page[p][0]
        print contentUrl
        title = page[p][1]
        content = getHtml(contentUrl, 2)
        print content = json.dumps(content, ensure_ascii=False, indent=2)
        savePost(title, wechat, content)
