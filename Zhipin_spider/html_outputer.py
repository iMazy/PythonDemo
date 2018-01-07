# -*- coding: utf-8 -*-
# @Time    : 2018/1/7 上午11:47
# @Author  : Mazy
# @File    : html_outputer.py
# @Software: PyCharm

from xlwt import Workbook, Worksheet
import xlsxwriter

class HtmlOutputer(object):

    # 使用 xlwt 将数据存到 Excel
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

    # 使用 xlsxwriter 将数据存到 Excel
    def save_to_excel_other_way(self, results, tag_names, file_name):
        book = xlsxwriter.Workbook(R'/Users/bai/Desktop/%s.xls' % file_name)
        tmp = book.add_worksheet()

        row_num = len(results)

        for i in range(1, row_num+1):
            if i == 1:
                tag_pos = 'A%s' % i
                tmp.write_row(tag_pos, tag_names)
            else:
                con_pos = 'A%s' % i
                content = results[i-1]
                tmp.write_row(con_pos, content)

        book.close()
