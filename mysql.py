# !/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb, time

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='',
        db ='test',
        use_unicode=1,
        charset='utf8'
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

title = "sdsd"
wechat = "sdsd"
content = "sd"
# content = "<p> 烤箱做的大多都是肉肉的菜，要么就是能量高的各种烘焙，选来选去，晚上能吃的，也只有虾啊贝啊这些能量稍低的了，废话不多说，开做。</p><p><strong>原料：</strong></p><p>鲜虾10个 口蘑6个 青红尖椒各半个 洋葱半个 大蒜3瓣</p><p></p><p><strong>调料：</strong>盐1/2茶匙（3克） 蚝油1茶匙（5ml） 糖1/3茶匙（约2克） 黄油15克 水淀粉1汤匙（15ml） 黑胡椒碎1茶匙（5克）</p><p><strong>做法：</strong></p><p>1）洋葱，大蒜洗净后切碎，青红椒去籽切成小块，口蘑洗净后也切小块。</p><p>2）锅中放入黄油，小火融化后加入食用油（25ml），放入洋葱碎，大蒜碎，用中小火炒香后，撒入盐，蚝油，糖，黑胡椒碎，水（50ml），用中火煮开后，倒入水淀粉沿着一个方向搅拌，稍微粘稠后关火。</p><p>3）虾剪掉虾枪，虾须，在背部切1/2刀取出虾线，冲洗干净后同青红椒块，口蘑，一同放入黑椒汁中腌15分钟后，放入铺有锡纸的烤盘上，薄薄刷一层油，放入烤箱的中层，用190度，烤25分钟左右。</p><p>4）烤好后撒上蒜碎即可。</p><p><strong>爱心小贴士：</strong></p><p>**黄油容易糊锅，记得用小火融化，然后再加一些食用油一起炒，既增香，也不容易糊。</p><p>**黑胡椒汁不要收的过于浓稠，出现粘稠的状态就可以了，不然没法腌渍虾和蔬菜哦。</p><p>**可以在拌好黑椒汁的虾和蔬菜上淋一些油，这样油把料汁包裹起来，食材会更加入味，烤好后味道更香。</p><p>**不喜欢蒜味的话，最后的蒜碎可以不用撒。</p><p>**黑胡椒一定要用现研磨的，黑胡椒粉没有黑胡椒粒自己研磨后的味道好哈。</p><p>**菜谱是以10个虾为参考，如果你做的多，其他的调料翻倍就行。</p><p>（内容图片均来自于文怡博客）<br /></p></div> "
today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
# cur.execute("INSERT INTO posts VALUES('99', %s, 'e', %s, %s, %s)", (title, wechat, content, today))

# cur.execute("CREATE TABLE IF NOT EXISTS `ewyu` (`gg` VARCHAR(50),`ff` VARCHAR(50))")

conn.set_character_set('utf8')
query = "insert into ewyu(gg,ff) values(%s , %s)"
para = ("中国","北京")
cur.execute(query,para)


#修改查询条件的数据
# cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
# cur.execute("delete from student where age='9'")

cur.close()
conn.commit()
conn.close()