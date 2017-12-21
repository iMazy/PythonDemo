# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 下午3:11
# @Author  : Mazy
# @File    : html_outputer.py
# @Software: PyCharm

class HtmlOutputer(object):

    def __init__(self):
        # 默认的标题，如果没有成功获取到标题的话则会用这个标题
        self.defaultTitle = u"百度贴吧"
        # 全局file变量，文件写入操作对象
        self.file = None
        # 楼层标号，初始为1
        self.floor = 1


    def outputer(self, title, contents, floorTag):

        self.setFileTitle(title)
        self.writeData(contents, floorTag)

    def setFileTitle(self, title):
        # 如果标题不是为None，即成功获取到标题
        if title is not None:
            self.file = open(title + ".txt", "w+", encoding='utf-8')
        else:
            self.file = open(self.defaultTitle + ".txt", "w+", encoding='utf-8')

    def writeData(self, contents, floorTag):
        # 向文件写入每一楼的信息
        for item in contents:
            if floorTag == "1":
                # 楼之间的分隔符
                floorLine = "\n" + str(
                    self.floor) + u"------------------------------------------------------------------------------------------------------\n"
                self.file.write(floorLine)
            print(item.decode("utf-8"))
            self.file.write(item.decode('utf-8'))
            self.floor += 1

