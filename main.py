from lib import mylog
from lib import mysql_py3 as mysql_db
import requests
import json

class SiteDetailImage:
    id = 0
    site_id = 0
    site_name = ''
    detail_page = ''

    def __init__(self, id, siteid, detail_page):
        pass


if __name__=='__main__':

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36', 'referer':'https://m.weibo.cn/msg/atme?subtype=allWB', 'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
    
    url = 'http://www.google.com'
    
    #获取第x条列表页
    r = requests.get(url)
    print (r.text)
    