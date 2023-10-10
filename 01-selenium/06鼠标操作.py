# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/9 15:33
# @File:02元素定位.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://baidu.com")  # 控制浏览器，访问百度
action =ActionChains(driver)
#点击右键
# action.context_click(driver.find_element(By.XPATH,"//*[@id='su']"))

#悬停
# action.move_to_element(driver.find_element(By.XPATH,"//*[@class='soutu-btn']"))
# action.perform()

#拖拽
# action.drag_and_drop(driver.find_element(By.ID,'div1'),driver.find_element(By.ID,'div2'))

time.sleep(5)
driver.quit()  # 关闭浏览器
