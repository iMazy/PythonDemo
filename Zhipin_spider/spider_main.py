# -*- coding: utf-8 -*-
# @Time    : 2018/1/7 上午11:47
# @Author  : Mazy
# @File    : spider_main.py
# @Software: PyCharm

from Zhipin_spider import html_downloader, html_parser, html_outputer
import time
import random

class BOSS_Main(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def start(self, baseURL, page_count):

        all_coms = []

        for i in range(1, page_count+1):
            time.sleep(random.uniform(1, 5))
            print("正在抓取第 %d 页数据" % i)
            content = self.downloader.get_page(baseURL, i, "ios")

            com_results = self.parser.parse(content)

            print(len(com_results))

            for com in com_results:
                all_coms.append(com)


        print(len(all_coms))
        print(all_coms)

        tag_name = ['公司名称', '职位名称', '工资', '所需学历', '公司介绍']
        # self.outputer.save_to_excel(all_coms, tag_name, "test")

        self.outputer.save_to_excel_other_way(all_coms, tag_name, "boss")

if __name__ == "__main__":
    print("请输入抓取页数：")
    pages = int(input())
    baseURL = "http://www.zhipin.com/job_detail/"
    bosszp = BOSS_Main()
    bosszp.start(baseURL, pages)
