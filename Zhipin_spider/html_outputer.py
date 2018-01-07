# -*- coding: utf-8 -*-
# @Time    : 2018/1/7 上午11:47
# @Author  : Mazy
# @File    : html_outputer.py
# @Software: PyCharm

from xlwt import Workbook, Worksheet

class HtmlOutputer(object):

    def save_to_excel(self, results, tag_name, file_name):

        book = Workbook(encoding="utf-8")

        tmp = book.add_sheet('sheet')

        times = len(results) + 1

        for i in range(times):
            if i==0 :
                for tag_name_i in tag_name:
                    tmp.write(i, tag_name.index(tag_name_i), tag_name_i)

            else:
                for tag_list in range(len(tag_name)):
                    tmp.write(i, tag_list, str(results[i-1][tag_list]))

        book.save(r'/Users/bai/Desktop/%s.xls' % file_name)