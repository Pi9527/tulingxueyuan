# 爬虫准备工作
- 参考资料
    - python网络数据采集,图灵工业出版
    - 精通Python爬虫狂阶Scrapy,人民邮电出版社
- 前提知识
    - Url
    - Http协议
    - Web前端,html,css,js
    - ajax
    - re, xpath
    - xml
# 爬虫简介
- 爬虫定义:百度
- 三大步骤:
    - 下载网页
    - 提取正确的信息
    - 根据一定规则自动跳到另外的网页上执行上两步内容
- 爬虫分来
    - 通用爬虫
    - 专用爬虫(聚焦爬虫)
    
- Python网络包简介
    - Python3.x:urllib, urllib3, httplib2, requests

# urllib
- 包含模块
    - urllib.request: 打开和读取url
    - urllib.error: 包含urllib.request产生的常见的错误,使用try捕捉
    - urllib.parse: 包含解析url的方法
    - urllib.robotparse:解析robots.txt文件
    - 案例01
- 网页编码问题解决
    - chardet 可以自动检测文件页面文件的编码格式,但是,可能有误
    - 需要安装,conda