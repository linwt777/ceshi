# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/9 15:33
# @File:02元素定位.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("file:///G:/Web-Test/selenium-test/%E8%AD%A6%E5%91%8A%E6%A1%86.html")  # 控制浏览器，访问百度
driver.maximize_window()
driver.find_element(By.XPATH,"//*[text()='点我']").click()
#警告框，切换到警告框，然后操作警告框
alert = driver.switch_to.alert
print(alert.text)
#操作
time.sleep(3)
alert.accept()
# alert.dismiss()

time.sleep(3)
driver.quit()  # 关闭浏览器
