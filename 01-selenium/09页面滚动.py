# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/9 15:33
# @File:02元素定位.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.douyu.com/directory/all")  # 控制浏览器，访问百度
driver.maximize_window()

#selenuim中并没有页面滚动，使用js代码
js_str='window.scrollTo(0,10000)'

driver.execute_script(js_str)

time.sleep(5)
driver.find_element(By.XPATH,"//*[text()='下一页']").click()

time.sleep(5)
driver.quit()  # 关闭浏览器
