# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/9 15:33
# @File:02元素定位.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://mail.qq.com")  # 控制浏览器，访问百度
driver.maximize_window()
driver.switch_to.frame(driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[1]/div/div[2]/div[2]/iframe"))

time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div[1]/div[10]/a[1]']").click()

time.sleep(3)
driver.find_element(By.XPATH,"//*[@id="u"]").send_keys("123456")

#返回原始页面
driver.switch_to.default_content()
time.sleep(3)
driver.quit()  # 关闭浏览器
