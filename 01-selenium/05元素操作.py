# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/9 15:33
# @File:02元素定位.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://baidu.com")  # 控制浏览器，访问百度


#xpath定位
# driver.find_element(By.XPATH,"//*[@id='kw']").send_keys("第一次")
# #清楚输入文字
# driver.find_element(By.XPATH,"//*[@id='kw']").clear()
#
# driver.find_element(By.XPATH,"//*[@id='kw']").send_keys("python")
# driver.find_element(By.XPATH,"//*[@id='su']").click()

print(driver.find_element(By.XPATH, "//*[@id='kw']").size)
print(driver.find_element(By.XPATH, "//*[@id='kw']").text)
print(driver.find_element(By.XPATH, "//*[@id='kw']").is_enabled())
print(driver.find_element(By.XPATH, "//*[@id='kw']").is_displayed())

print(driver.find_element(By.XPATH, "//*[text()='新闻']").get_attribute('href'))

time.sleep(5)
driver.quit()  # 关闭浏览器
