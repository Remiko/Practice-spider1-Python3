# -*- coding: UTF-8 -*-
from urllib import request, error
import re


regex1 = r'href="(https://news.sina.com.cn/.*?.shtml)"'  # 爬取新浪每个主页上的新闻链接的正则
regex2 = r'\<p\>\s*(.*?)\</p>'  # 爬取每篇新闻的文章的正则
start_url = 'https://news.sina.com.cn/'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15'
                  ' Safari/537.36'
}  # 伪装自己为谷歌浏览器
data_1 = request.urlopen(start_url)
html_1 = data_1.read().decode('utf-8')  # 爬取出
regex_url = re.compile(regex1)
regex_url_result = regex_url.findall(html_1)  # 筛选出新闻的链接，只为一个list

for i in range(len(regex_url_result)):
    try:
        new_url = regex_url_result[i]
        req = request.Request(new_url, headers=headers)  # 给请求加上header头
        rsp = request.urlopen(req)
        html_news = rsp.read().decode('utf-8')
        regex_url_article = re.compile(regex2)
        regex_url_article_result = regex_url_article.findall(html_news)
        with open(r'D:\PyPractice\Reptile\news\news.txt', 'a', encoding='utf-8') as f:
            for j in range(len(regex_url_article_result)):
                regex_url_article_result[j] = regex_url_article_result[j].replace('<strong>', '')
                regex_url_article_result[j] = regex_url_article_result[j].replace('</strong>', '')
                f.write(regex_url_article_result[j])
                f.write('\n')
            f.write('\n\n\n')
        print('第{0}个文章爬取成功'.format(i + 1))

    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
