# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 下午1:58
# @Author  : Mazy
# @File    : html_outputer.py
# @Software: PyCharm

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if  data is None:
            return
        self.datas.append(data)

    def output_html(self):

        file = open('output.txt','w+', encoding='utf-8')

        for  data in self.datas:
            file.write("-----------------------------------------------------------------" + "\n")
            file.write(data['title'] + '\n')
            file.write(data['url'] + '\n')
            file.write(data['summary'] + '\n')


        print("输出完成，请打开当前文件目录下的 output.txt 文件查看内容")