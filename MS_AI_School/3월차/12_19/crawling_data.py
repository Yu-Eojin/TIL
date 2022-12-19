### 데이터 수집하기위한 크롤링 코드 ###
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from multiprocessing import Pool
import pandas as pd
import os
import time
import urllib.request

# 키워드 가져오기
keys = pd.read_csv(
    "C:/Users/user/Desktop/MS_AI_School/TIL/MS_AI_School/3월차/12_19/keyword.txt", 
    names=['keyword'])
keyword = []
[keyword.append(keys['keyword'][x]) for x in range(len(keys))]

print(keyword)


def create_folder(dir):
    # 이미지저장할 폴더 구성
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
    except OSError:
        print("Error creating folder", + dir)


def image_download(keyword):
    # image download 함수
    create_folder("./" + keyword + "/")

    # chromdriver 가져오기
    chromdriver = "C:/Users/user/Desktop/MS_AI_School/TIL/MS_AI_School/3월차/12_19/chromedriver.exe"
    driver = webdriver.Chrome(chromdriver)
    driver.implicitly_wait(3)

    print("keyword: " + keyword)
    driver.get('https://www.google.co.kr/imghp?hl=ko')
    keywords = driver.find_element(By.XPATH,
        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    keywords.send_keys(keyword)
    driver.find_element(By.XPATH,
        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button').click()

    print(keyword+' 스크롤 중 .............')
    elem = driver.find_element(By.TAG_NAME,"body")
    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)

    try:
        driver.find_element(By.XPATH,
            '//*[@id="islmp"]/div/div/div/div[2]/div[1]/div[2]/div[2]/input').click()
        for i in range(60):
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.1)
    except:
        pass

    images = driver.find_elements(By.CSS_SELECTOR,"img.rg_i.Q4LuWd")
    print(keyword+' 찾은 이미지 개수:', len(images))

    links = []
    for i in range(1, len(images)):
        try:
            print('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img')

            driver.find_element(By.XPATH,
                '//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').click()
            links.append(driver.find_element(By.XPATH,
                '//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img').get_attribute('src'))
            # driver.find_element_by_xpath('//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a').click()
            print(keyword+' 링크 수집 중..... number :'+str(i)+'/'+str(len(images)))
        except:
            continue

    forbidden = 0
    for k, i in enumerate(links):
        try:
            url = i
            start = time.time()
            urllib.request.urlretrieve(
                url, "./"+keyword+"/"+str(k-forbidden)+".jpg")
            print(str(k+1)+'/'+str(len(links))+' '+keyword +
                  ' 다운로드 중....... Download time : '+str(time.time() - start)[:5]+' 초')
        except:
            forbidden += 1
            continue
    print(keyword+' ---다운로드 완료---')

    driver.close()


# =============================================================================
# 실행
# =============================================================================
if __name__ == '__main__':
    pool = Pool(processes=5)  # 5개의 프로세스를 사용합니다.
    pool.map(image_download, keyword)


