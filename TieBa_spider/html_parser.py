# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 下午3:11
# @Author  : Mazy
# @File    : html_parser.py
# @Software: PyCharm

import re
from TieBa_spider import tools

class HtmlParser(object):

    def __init__(self):
        self.tool = tools.Tool()

    def parser(self, html_content):
        title = self.get_title(html_content)
        page_count = self.get_page_num(html_content)
        content = self.get_contents(html_content)

        return title, page_count, content


    def get_title(self, html_content):
        # page = self.getPage(1)
        # <h3 class="core_title_txt pull-left text-overflow  " title="纯原创我心中的NBA2014-2015赛季现役50大" style="width: 396px">纯原创我心中的NBA2014-2015赛季现役50大</h3>
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>', re.S)
        result = re.search(pattern, html_content)
        if result:
            # print(result.group(1).strip())
            return result.group(1).strip()
        else:
            return None

    # 获取帖子一共有多少页
    def get_page_num(self, html_content):
        # page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num".*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, html_content)
        if result:
            # print(result.group(1))
            return result.group(1).strip()
        else:
            return None

    # 获取每一层楼的内容,传入页面内容
    def get_contents(self, html_content):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, html_content)
        contents = []
        for item in items:
            # print(item)
            # print(self.tool.replace(item))
            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content.encode("utf-8"))
        return contents