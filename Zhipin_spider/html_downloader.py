# -*- coding: utf-8 -*-
# @Time    : 2018/1/7 上午11:46
# @Author  : Mazy
# @File    : html_downloader.py
# @Software: PyCharm


import requests
import ssl

class HtmlDownloader(object):

    # 初始化方法，定义一些变量
    def __init__(self):
        ssl._create_default_https_context = ssl._create_unverified_context

    # 通过 url + 页码 + 关键词 获取数据
    def get_page(self, baseUrl, page_num, keyword):
        try:
            param = {"query": keyword, "city": "101010100", "page": page_num}

            # 设置请求头，模拟浏览器访问
            header = {
                'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                              r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
                'Referer': r'http://www.zhipin.com/job_detail/',
                'Connection': 'keep-alive'
            }

            result = requests.get(baseUrl, params=param, headers=header)

            # print(result.text)

            return result.text

        except Exception as err:
            print(err)
            print("Boss直聘爬取失败")
            return None
