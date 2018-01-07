# -*- coding: utf-8 -*-
# @Time    : 2018/1/7 上午11:47
# @Author  : Mazy
# @File    : html_parser.py
# @Software: PyCharm

from bs4 import BeautifulSoup

class HtmlParser(object):

    def parse(self, html_content):
        if html_content is None:
            return None

        soup = BeautifulSoup(html_content, 'html.parser')
        # 获取公司的列表
        companies = soup.find('div', class_='job-list').select('ul > li')

        results = []
        for com in companies:
            res = self.get_one_company(com)
            results.append(res)

        return results


    def get_one_company(self, soup):

        # company name
        com_name = soup.find('div', class_="info-company").find('a').text
        # job name
        all = soup.find('div', class_="info-primary").find('h3', class_="name").a.text
        sala = soup.find('div', class_="info-primary").find('h3', class_="name").a.span.text
        job = all.replace(sala, "")

        salary = soup.find('div', class_="info-primary").find('h3', class_="name").a.span.text
        # conpany require
        job_require = soup.find('div', class_="info-primary").find('p').text

        # company desc
        com_desc = soup.find('div', class_="info-company").find('p').text

        return [com_name, job, salary, job_require, com_desc]