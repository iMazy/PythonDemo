# -*- coding: utf-8 -*-
# @Time    : 2018/1/7 上午11:47
# @Author  : Mazy
# @File    : spider_main.py
# @Software: PyCharm

from Zhipin_spider import html_downloader


class BOSS_Main(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()

    def start(self):
        baseURL = "http://www.zhipin.com/job_detail/"
        self.downloader.get_page(baseURL, "1", "ios")

if __name__ == "__main__":
    print("请输入贴子代号：")
    baseURL = "http://www.zhipin.com/job_detail/"
    bosszp = BOSS_Main()
    bosszp.start()
