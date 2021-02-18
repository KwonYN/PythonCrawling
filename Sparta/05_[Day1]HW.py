from bs4 import BeautifulSoup
from selenium import webdriver
import dload
import time

driver = webdriver.Chrome('chromedriver')
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%EC%97%90%EC%9D%B4%ED%94%84%EB%A6%B4+%EB%A0%88%EC%9D%B4%EC%B2%BC") # 여기에 URL을 넣어주세요
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

###################################
# 이제 여기에 코딩을 하면 됩니다!
###################################

#imgList > div:nth-child(1) > a > img
#imgList > div:nth-child(76) > a > img

pics = soup.select('#imgList > div > a > img')
pic_count = 0
for pic in pics:
    thumbnail = pic['src']
    pic_count += 1
    dload.save(thumbnail, f'imgs_homework_april_rachel/{pic_count}.jpg')
    print(thumbnail)

driver.quit() # 끝나면 닫아주기