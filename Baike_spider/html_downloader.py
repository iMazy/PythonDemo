# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 下午1:58
# @Author  : Mazy
# @File    : html_downloader.py
# @Software: PyCharm

import urllib.request

class HtmlDownloader(object):

    def html_downloader(self, url):
        if url is None:
            return

        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            return html