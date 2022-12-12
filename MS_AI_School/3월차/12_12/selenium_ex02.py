from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from multiprocessing import Pool
import time
import os
import urllib.request
import pandas as pd

'''
폴더구성
'''
def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('error : Creating directory...' + directory)

# 검색 키워드 호출
key = pd.read_csv('./keyword.txt', names=['keyword'])
keyword = []
[keyword.append(key['keyword'][x]) for x in range(len(key))]


def img_download(keywords) :
    create_folder('./'+keywords+'_low_resolution')

    # 크롬 드라이버 호출
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    chromedriver = './chromedriver'
    driver = webdriver.Chrome(chromedriver, options=options)
    driver.implicitly_wait(3)
    
    # 검색
    print('검색 >> ' , keywords)
    driver.get("https://www.google.co.kr/imghp?h1=ko")
    keyword = driver.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    keyword.send_keys(keywords)
    keyword.send_keys(Keys.RETURN)

    # 스크롤 내리기 + 더보기 클릭
    print('스크롤 ......', keywords)
    elem = driver.find_element(By.TAG_NAME, 'body')
    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)

    try :
        # 더보기 클릭
        driver.find_element(By.XPATH, 
            '//*[@id="islmp"]/div/div/div/div[2]/div[1]/div[2]/div[2]/input').click()
        for i in range(60):
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)  
    except:
        pass

    links = []
    images = driver.find_elements(By.CSS_SELECTOR, 'img.rg_i.Q4LuWd')

    
    ## 썸네일로 이미지 가져오기 ##
    for image in images:
        if image.get_attribute('src') != None:
            links.append(image.get_attribute('src'))

    print(keywords + '찾은 이미지 개수 : ', + len(links))
    time.sleep(2)

    create_folder('./'+keywords+'_low_resolution')
    for index, i in enumerate(links):
        url = i
        start = time.time()
        urllib.request.urlretrieve(
            url, "./" + keywords + "_low_resolution/" + keywords + "_" + str(index) + ".jpg")
        print(str(index+1) + "/" + str(len(links)) + " " + keywords +
              " 다운로드 시간 ------ : ", str(time.time() - start)[:5] + '초')
    print("다운로드 완료 !!!!")

## 실행 ##
if __name__ == '__main__':
    pool = Pool(processes=3)
    pool.map(img_download, keyword)
