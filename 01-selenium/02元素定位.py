# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/9 15:33
# @File:02元素定位.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://baidu.com")  # 控制浏览器，访问百度
# 根据id查询
# driver.find_element(By.ID, 'kw').send_keys("美女")
# driver.find_element(By.ID, 'su').click()
#
# # 根据name查询
# driver.find_element(By.NAME, 'wd').send_keys("美女")
# driver.find_element(By.ID, 'su').click()
# #根据classname查找
# driver.find_element(By.CLASS_NAME,"s_ipt").send_keys("美女")
# driver.find_element(By.ID, 'su').click()

#根据a标签查询
# driver.find_element(By.LINK_TEXT,"hao123").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"hao12").click()

#css选择器定位
# driver.find_element(By.CSS_SELECTOR,"#su").click()
# time.sleep(5)

#xpath定位
driver.find_element(By.XPATH,"//*[@id='kw']").send_keys("第一次")
driver.find_element(By.XPATH,"//*[@id='su']").click()

time.sleep(5)
driver.quit()  # 关闭浏览器
