# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用Requests 爬取微信搜狗的文章
import sys, requests, time, re, json, xmltodict, model


class Weixin():

	# 获取标题、日期、正文内容
	def get_content(self, url):
		r = requests.get(url)
		r.encoding = 'utf-8'
		rules = re.compile('[\s\S]*<div class="rich_media_inner">[\s\S]*id="activity-name">(.*?)</h2>[\s\S]*<em id="post-date" class="rich_media_meta text">(.*?)</em>[\s\S]*<div class="rich_media_content" id="js_content">(.*?)</div>[\s\S]*</div>')
		page = re.findall(rules, r.content)
		if page:
			# return page[0]
			# 返回正文
			return page[0][2]
		else:
			return False

	def build(self, openid):
		url = 'http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=%s&page=%d&t=%d'
		# 获得当前时间时间戳
		now = int(time.time())
		print '开始爬取……'
		r = requests.get(url % (openid, 1, now))  # 发送请求
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
		    f['pubDate'] = time.strftime("%Y-%m-%d", pubdate)
		    # f['pubDate'] = time.strftime("%Y-%m-%d %H:%M:%S", pubdate)
		    print '开始爬取正文……'
		    f['content'] = self.get_content(f['link'])
		    print '准备保存数据库……'
		    if f['content']:
		    	model.save_post(f['title'], f['creator'], f['pubDate'], 'readeep', f['content'])
		    else:
		    	print '-------《%s》文章正文抓取失败' % unicode(f['title']).encode('utf-8')

		    # print f
		    # exit()
		    # f.feed['item'].append(f.item.copy())


# 调试
def pretty_json(obj):
    # return json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False)
    return json.dumps(obj, sort_keys=True, indent=2)


def test():
    w = Weixin()
    w.build('oIWsFt3YPNgmME4kAjhBzMATTnP8')


if __name__ == '__main__':
	test()