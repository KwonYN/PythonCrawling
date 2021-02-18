from bs4 import BeautifulSoup
from selenium import webdriver  # 웹페이지 조작 및 스크래핑

from openpyxl import Workbook   # 엑셀 조작

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders      # 이메일 보내기

# 크롬 열기
driver = webdriver.Chrome('chromedriver')

# 엑셀 열고 조작
wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사", "썸네일"])

# 기사 스크래핑 준비
url = f"https://search.naver.com/search.naver?&where=news&query=%EC%82%BC%EC%84%B1SDS&sm=tab_tmr&frm=mr&nso=so:r,p:all,a:all&sort=0"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

# 엑셀에 씀
#main_pack > div.news.mynews.section._prs_nws > ul
#sp_nws1 > dl > dt > a
#sp_nws6 > dl > dt > a
#sp_nws2 > div > a > img
articles = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul > li')
for each_article in articles:
    article = each_article.select_one('dl > dt > a')

    publising_company = each_article.select_one('dl > dd.txt_inline > span._sp_each_source').text.split(' ')[0].replace('언론사', '')
    article_title = article.text
    article_url = article['href']
    article_pic = each_article.select_one('div > a > img')
    if article_pic is None:
        article_pic = "No Image"
    else:
        article_pic = article_pic['src']

    print(f'{article_title}[{publising_company}] : {article_url} ({article_pic})')
    ws1.append([article_title, article_url, publising_company, article_pic])

# 엑셀 저장
wb.save(filename='sds_articles.xlsx')
driver.quit()

# 이메일 보내기!!

# 보내는 사람 정보 : 써야함!
me = ""
my_password = ""

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보
emails_list = ["email1@naver.com", "email2@naver.com", "email3@gmail.com"]
for you in emails_list:
    # 메일 기본 정보 설정
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "[] 기사 동향"
    msg['From'] = me
    msg['To'] = you

    # 메일 내용 쓰기
    content = "기사 동향 파악"
    part2 = MIMEText(content, 'plain')
    msg.attach(part2)

    # 파일 첨부하기
    part = MIMEBase('application', "octet-stream")
    with open("sds_articles.xlsx", 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment", filename="기사 동향")
    msg.attach(part)

    # 메일 보내고 서버 끄기
    s.sendmail(me, you, msg.as_string())

s.quit()