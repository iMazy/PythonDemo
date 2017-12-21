# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 下午3:10
# @Author  : Mazy
# @File    : html_downloader.py
# @Software: PyCharm

import urllib.request

class HtmlDownloader(object):

    def get_page(self, baseUrl, onlyLZ, page_num):
        try:
            url = baseUrl + onlyLZ + '&pn=' + str(page_num)
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            # print(response.read().decode("utf-8"))
            return response.read().decode('utf-8')
        except Exception as err:
            print(err)
            print("链接百度贴吧失败")
            return None