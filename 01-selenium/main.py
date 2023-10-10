# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # 新增
import time

driver = webdriver.Chrome()


driver.get("https://baidu.com") #控制浏览器，访问百度

time.sleep(5)

driver.quit() #关闭浏览器
