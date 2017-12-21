# PythonDemo
Demo by python

### Baike_spider
#### 目录结构：
```
|-- Baike_spider（文件夹）
   |-- spider_main.py（爬虫调度器————程序入口，管理各个模块）
   |-- url_manager.py（URL 管理器————管理 url）
   |-- html_downloader.py （网页下载器————通过url获取网页内容）
   |-- html_parser.py （网页解析器————通过网页内容解析出新的 url 和 新的内容）
   |-- html_outputer.py （输出————将获取到的数据输出）

```
***
#### 用到的知识点：
- 使用 urllib 请求数据
- 使用 BeautifulSoup 解析网页
- 使用 re 正则匹配 url 数据
- 使用 urljoin 将拼接 url
