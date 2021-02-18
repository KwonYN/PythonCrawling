from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

#####################
# 여기에 코드 적기!
#####################

#sp_nws1 > dl > dt > a
    #sp_nws1 > dl > dd:nth-child(3)
#sp_nws6 > dl > dt > a
#sp_nws19 > dl > dt > a
article = soup.select_one('#sp_nws1 > dl > dt > a')
print(article.text)
# parameter : article.text => text 타입의 속성만 가지고 오는 것!
#           : article['title'] => 'title'이라는 속성을 가지고 옴!

print('=====================')

#main_pack > div.news.mynews.section._prs_nws > ul

#sp_nws1 > dl > dd.txt_inline > span._sp_each_source

articles = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul > li')
for each_article in articles:
    article = each_article.select_one('dl > dt > a')
    publising_company = each_article.select_one('dl > dd.txt_inline > span._sp_each_source').text.split(' ')[0].replace('언론사', '')
    title = article.text
    url = article['href']
    print(f'{title}[{publising_company}] : {url}')

driver.quit()