# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 下午1:58
# @Author  : Mazy
# @File    : html_parser.py
# @Software: PyCharm

from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

class HtmlParser(object):

    def parse(self, page_url, html_content):
        if  page_url is None or html_content is None:
            return

        soup = BeautifulSoup(html_content, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_date(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):

        new_urls = set()
        # 查找 a 标签
        links = soup.findAll('a', href=re.compile(r"/item/[0-9a-zA-Z]+$"))

        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)

        return new_urls

    def _get_new_date(self, page_url, soup):

        res_data = {}

        # url
        res_data['url'] = page_url
        print(page_url)

        # title
        # <dd class="lemmaWgt-lemmaTitle-title">
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        print(title_node.get_text())

        # summary
        # body > div.body-wrapper > div.content-wrapper > div > div.main-content > div.lemma-summary
        summary_node = soup.find("div", class_='lemma-summary')
        print(summary_node.get_text())

        res_data['title'] = title_node.get_text()
        res_data['summary'] = summary_node.get_text()

        return res_data