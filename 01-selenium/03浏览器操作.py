# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/9 21:50
# @File:03浏览器操作.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = "https://baidu.com"

driver.get(url)

#最大化浏览器
driver.maximize_window()
#设置浏览器宽高
driver.set_window_size(980,1080)
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='kw']").send_keys("123")
driver.find_element(By.XPATH,"//*[@id='su']").click()
time.sleep(2)
#浏览器后退
driver.back()
time.sleep(2)
#浏览器前进
driver.forward()
time.sleep(2)
#刷新浏览器
driver.refresh()
time.sleep(2)
driver.back()
driver.find_element(By.XPATH,"//*[text()='hao123']").click()
time.sleep(2)
#关闭当前页面
driver.close()

time.sleep(3)
driver.quit()