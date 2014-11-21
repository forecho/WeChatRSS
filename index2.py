# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用Requests 爬取微信搜狗的文章
import sys, requests, time, re, json, xmltodict


class Weixin():

	# 获取标题、日期、正文内容
	def get_content(self, url):
		# r = requests.get(url)
		r = requests.get('http://mp.weixin.qq.com/s?__biz=MjM5ODc5OTQ0MA==&mid=201056223&idx=1&sn=a885f4ae7427e803fa8bb54deeb6a4be&3rd=MzA3MDU4NTYzMw==&scene=6#rd')
		r.encoding = 'utf-8'
		rules = re.compile('<div class="rich_media_inner">[\s\S]*id="activity-name">(.*?)</h2>[\s\S]*<em id="post-date" class="rich_media_meta text">(.*?)</em>[\s\S]*<div class="rich_media_content" id="js_content">(.*?)</div>[\s\S]*</div>')
		print re.findall(rules, r.content)
		# exit()
		return re.findall(rules, r.content)

	def build(self, openid):
		url = 'http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=%s&page=%d&t=%d'
		# 获得当前时间时间戳
		now = int(time.time())
		r = requests.get(url % ('oIWsFt3YPNgmME4kAjhBzMATTnP8', 1, now))  # 发送请求

		obj = re.findall(r'\nsogou.weixin.gzhcb\((\{.+\})\)', r.content)
		items = json.loads(obj[0])['items']

		for item in items:
		    item = xmltodict.parse(item)

		    # print pretty_json(item)
		    f = {}
		    f['title'] = item['DOCUMENT']['item']['display']['title']
		    f['link'] = item['DOCUMENT']['item']['display']['url']
		    f['guid'] = item['DOCUMENT']['item']['display']['docid']
		    f['description'] = item['DOCUMENT']['item']['display']['content168']
		    f['creator'] = item['DOCUMENT']['item']['display']['sourcename']

		    pubdate = time.localtime(float(item['DOCUMENT']['item']['display']['lastModified']))
		    f['pubDate'] = time.strftime("%a, %d %b %Y %H:%M:%S +0000", pubdate)
		    f['content'] = self.get_content(f['link'])
		    print '开始爬取……'
		    # f.feed['item'].append(f.item.copy())

		# file_object = open('thefile.txt', 'a+')
		# file_object.write('items')
		# file_object.close()

		# print items
		# repr(obj)
		print json.loads(obj[0])['items']

		print type(obj)
		print len(obj)
		encodedjson = json.dumps(obj)
		s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
		# decodejson = json.loads(encodedjson)
		decodejson = json.loads(encodedjson)
		# print s.keys()
		# print json.loads(encodedjson).keys()
		print type(s)
		print type(encodedjson)
		print type(decodejson)
		# print obj[1]
		# print items.r.json()['items'][0]
		# print r.url
		# print r.content


# 调试
def pretty_json(obj):
    # return json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False)
    return json.dumps(obj, sort_keys=True, indent=2)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
    	self.get_a("s")
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_a(a):
    	print a

def test():
    # w = Weixin('oIWsFt3YPNgmME4kAjhBzMATTnP8')
    w = Weixin()
    w.build('oIWsFt3YPNgmME4kAjhBzMATTnP8')
    # w.pretty_json('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
    # print w.pretty_json('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
    # print w.search_result
	# p = Point(2,3)
	# print p.distance_from_origin()


if __name__ == '__main__':
	test()