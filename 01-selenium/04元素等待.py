# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # 新增
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()


driver.get("https://baidu.com") #控制浏览器，访问百度

driver.find_element(By.ID, 'kw').send_keys("美女")
driver.find_element(By.ID, 'su').click()

#进行页面等待
#3种 强制，显式，隐式
#强制
# time.sleep(3)

#显式
#等待某个元素加载完成，每隔0.5秒加载一次，最多加载5秒
# WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"//*[@class='image-content_1csSY']")))

#隐式
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//*[@class='image-content_1csSY']").click()

time.sleep(2)

driver.quit() #关闭浏览器
