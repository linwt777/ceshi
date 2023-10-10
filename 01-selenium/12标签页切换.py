# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/9 15:33
# @File:02元素定位.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://baidu.com")  # 控制浏览器，访问百度
driver.maximize_window()

print(driver.window_handles)
print(driver.current_window_handle)

driver.find_element(By.ID, 'kw').send_keys("美女")
driver.find_element(By.ID, 'su').click()

driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//*[@class='image-content_1csSY']").click()

print(driver.window_handles)
print(driver.current_window_handle)

#切换页面
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='srcPic']/img").click()
time.sleep(1)
driver.get_screenshot_as_file('1.png')

time.sleep(3)
driver.quit()  # 关闭浏览器
