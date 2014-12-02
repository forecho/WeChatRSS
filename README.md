主要使用 Python 写爬虫，暂时先爬取 [chuansongme.com](http://www.chuansongme.com) 网站的资源和搜狗提供的资料。

**使用：**

1. [可能需要安装开发版Python](http://stackoverflow.com/questions/11094718/error-command-gcc-failed-with-exit-status-1-while-installing-eventlet)
1. [安装pip](http://o.forecho.com/blog/2014/11/18/install-pip/)
1. MySQL 数据库
1. [Flask](http://flask.pocoo.org/) 框架
1. [Flask](http://flask.pocoo.org/) 默认支持的 [jinja2]  (http://jinja.pocoo.org/) 模板
1. [Flask-MySQL](http://flask-mysql.readthedocs.org/en/latest/) 扩展
1. MySQLdb 库
1. [Requests: HTTP for Humans](http://requests.readthedocs.org/zh_CN/latest/user/install.html#install)
1. [xmltodict](https://github.com/martinblech/xmltodict) 解析XML

**安装**

1. `sudo apt-get install python-dev`
1. `sudo apt-get install python-pip`
1. `sudo pip install flask`
2. `sudo pip install flask-mysql`
2. `sudo pip install requests`
2. `sudo pip install xmltodict`


**初始化**

1. 修改 sql.py 文件配置，执行 `python sql.py`