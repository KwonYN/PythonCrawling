from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook

driver = webdriver.Chrome('chromedriver')
url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"
driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사"]) # 한 행 추가! (리스트 내 각 요소가 한 컬럼)

articles = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul > li')
for each_article in articles:
    article = each_article.select_one('dl > dt > a')
    publising_company = each_article.select_one('dl > dd.txt_inline > span._sp_each_source').text.split(' ')[0].replace('언론사', '')
    article_title = article.text
    article_url = article['href']
    print(f'{article_title}[{publising_company}] : {article_url}')
    ws1.append([article_title, article_url, publising_company])

driver.quit()
wb.save(filename='articles.xlsx')

