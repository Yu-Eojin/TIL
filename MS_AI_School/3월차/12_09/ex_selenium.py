from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.google.com')

elem = driver.find_element(By.NAME,'q')
elem.clear()
search = 'banana'
elem.send_keys(search)
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
elem.send_keys(Keys.RETURN)

assert 'No results found.' not in driver.page_source



input()