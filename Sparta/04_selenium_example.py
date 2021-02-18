# from selenium import webdriver
# driver = webdriver.Chrome('chromedriver')
#
# driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%95%84%EC%9D%B4%EC%9C%A0 ")

from bs4 import BeautifulSoup
from selenium import webdriver
import dload
import time
# selenium : Browser를 자동제어
# BeautifulSoup : Browser에 떠있는 것들 중 내가 원하는 것들을 솎아내는 것

driver = webdriver.Chrome('chromedriver') # 웹드라이버 파일의 경로
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%EB%A0%88%EB%93%9C%EB%B2%A8%EB%B2%B3+%EC%8A%AC%EA%B8%B0")
time.sleep(5) # 5초 동안 페이지 로딩 기다리기

req = driver.page_source
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(req, 'html.parser')

###################################
# 이제 여기에 코딩을 하면 됩니다!
###################################

# imgList > div:nth-child(1) > a > img
thumbnails = soup.select('#imgList > div > a > img')
thumbnails_cnt = 0
for thumb in thumbnails:
    img = thumb['src']
    thumbnails_cnt += 1
    file_directory = 'seulkey/'
    # dload.save(img, file_directory+str(thumbnails_cnt)+'.jpg')
    dload.save(img, f'seulkey/{thumbnails_cnt}.jpg')

driver.quit() # 끝나면 닫아주기