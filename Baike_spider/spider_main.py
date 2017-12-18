# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 下午1:57
# @Author  : Mazy
# @File    : spider_main.py
# @Software: PyCharm


from Baike_spider import html_downloader, html_parser, html_outputer, url_manager
import ssl

class SpiderMain(object):

    def __init__(self):

        # 添加环境变量
        ssl._create_default_https_context = ssl._create_unverified_context

        self.urlsManager = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()


    def craws(self, root_url, limit):
        count = 1
        self.urlsManager.add_new_url(root_url)

        while self.urlsManager.has_new_url():
            try:
                new_url = self.urlsManager.get_new_url()

                html_content = self.downloader.html_downloader(new_url)
                new_urls, new_data  = self.parser.parse(new_url, html_content)

                self.urlsManager.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == int(limit):
                    break

                count = count + 1

            except Exception as err:
                print(err)
                print('craw failed')
        # 文件输出
        self.outputer.output_html()



if __name__ == "__main__":

    entry = input('请输入你要抓取的词条:')
    limit = input('请输入你需要抓取的数量:')

    root_url = root_url = "https://baike.baidu.com/item/" + entry

    obj_spider = SpiderMain()
    obj_spider.craws(root_url, limit)