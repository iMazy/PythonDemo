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

        company_soup = soup.find('div', class_="info-company")
        # company name
        com_name = company_soup.find('a').text
        # company desc
        com_desc = company_soup.find('p').text


        primary_soup = soup.find('div', class_="info-primary")
        # job name
        all = primary_soup.find('h3', class_="name").a.text
        sala = primary_soup.find('h3', class_="name").a.span.text
        job = all.replace(sala, "")
        # salary
        salary = primary_soup.find('h3', class_="name").a.span.text
        # conpany require
        job_require = primary_soup.find('p').text

        return [com_name, job, salary, job_require, com_desc]