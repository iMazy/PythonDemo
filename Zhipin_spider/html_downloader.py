# -*- coding: utf-8 -*-
# @Time    : 2018/1/7 上午11:46
# @Author  : Mazy
# @File    : html_downloader.py
# @Software: PyCharm


import requests
import ssl

class HtmlDownloader(object):

# http://www.zhipin.com/job_detail/?query=swift&scity=101010100&source=2
# http://www.zhipin.com/job_detail/?query=ios&scity=101010100
# http://www.zhipin.com/c100010000/?query=ios&page=2&ka=page-2
# http://www.zhipin.com/c101010100/h_101010100/?query=ios&page=3&ka=page-3
# https://www.zhipin.com/c101010100/h_101010100/?query=ios&page=4

    # 初始化方法，定义一些变量
    def __init__(self):
        ssl._create_default_https_context = ssl._create_unverified_context

    def get_page(self, baseUrl, page_num, keyword):
        try:
            param = {"query": keyword, "city": "101010100", "page": page_num}

            # 设置请求头，模拟浏览器访问
            header = {
                'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                              r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
                'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
                'Connection': 'keep-alive'
            }

            result = requests.get(baseUrl, params=param, headers=header)

            print(result.text)

            return result.text
        except Exception as err:
            print(err)
            print("Boss直聘爬取失败")
            return None


boss_spider = HtmlDownloader()
boss_spider.get_page("http://www.zhipin.com/job_detail/", "1", "ios")