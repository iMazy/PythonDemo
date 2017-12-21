# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 下午3:10
# @Author  : Mazy
# @File    : spider_main.py
# @Software: PyCharm

import ssl
from TieBa_spider import tools, html_downloader, html_outputer, html_parser

class BDTB(object):

    # 出还刷，传入基地址，是否只看楼主的参数
    def __init__(self, baseUrl, seeLZ, floorTag):
        # base链接地址
        self.baseUrl = baseUrl
        # 是否只看楼主
        self.onlyLZ = '?see_lz=' + str(seeLZ)
        # HTML标签剔除工具类对象
        self.tool = tools.Tool()
        # 是否写入楼分隔符的标记
        self.floorTag = floorTag

        # 环境变量
        ssl._create_default_https_context = ssl._create_unverified_context

        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def start(self):

        content = self.downloader.get_page(self.baseUrl, self.onlyLZ, 1)
        page_count = self.parser.get_page_num(content)
        title =  self.parser.get_title(content)


        contents = []
        if page_count == None:
            print("URL已失效，请重试")
            return
        try:
            print("该帖子共有" + str(page_count) + "页")
            for i in range(1, int(page_count) + 1):
                print("正在写入第" + str(i) + "页数据")
                page = self.downloader.get_page(self.baseUrl, self.onlyLZ, i)
                content = self.parser.get_contents(page)
                for c in content:
                    contents.append(c)
            self.outputer.outputer(title, contents, self.floorTag)
        # 出现写入异常
        except IOError as err:
            print("写入异常，原因" + err.message)
        finally:
            print("写入任务完成")




if __name__ == "__main__":
    print("请输入贴子代号：")
    baseURL = "http://tieba.baidu.com/p/" + str(input())
    seeLZ = input('是否只获取楼主发言，是输入1，否输入0\n')
    floorTag = input("是否写入楼层信息，是输入1，否输入0\n")
    bdtb = BDTB(baseURL, seeLZ, floorTag)
    bdtb.start()