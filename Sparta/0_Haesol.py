from bs4 import BeautifulSoup
from selenium import webdriver  # 웹페이지 조작 및 스크래핑

# 엑셀 조작
import openpyxl
from openpyxl import Workbook
import datetime

# today
now = str(datetime.datetime.now()).split("-")
if int(now[1])-1 < 10:
    mth = '0'+str(int(now[1])-1)
else:
    mth = str(int(now[1])-1)
ym = now[0]+mth

# 엑셀 열고 조작
# wb = Workbook()
wb = openpyxl.load_workbook(f'출석부_해솔반_{ym}.xlsx')
ws1 = wb.active
ws1.title = f'출석부_해솔반_{ym}'
ws1.append(["제목", "링크", "신문사", "썸네일"])

# # 엑셀에 씀
# articles = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul > li')
# for each_article in articles:
#     article = each_article.select_one('dl > dt > a')
#
#     publising_company = each_article.select_one('dl > dd.txt_inline > span._sp_each_source').text.split(' ')[0].replace('언론사', '')
#     article_title = article.text
#     article_url = article['href']
#     article_pic = each_article.select_one('div > a > img')
#     if article_pic is None:
#         article_pic = "No Image"
#     else:
#         article_pic = article_pic['src']
#
#     print(f'{article_title}[{publising_company}] : {article_url} ({article_pic})')
#     ws1.append([article_title, article_url, publising_company, article_pic])
#
# # 엑셀 저장
wb.save(filename=f'출석부_해솔반_{ym}.xlsx')