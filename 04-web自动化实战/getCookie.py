# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/15 11:20
# @File:getCookie.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time,json,os
url = "https://user.qunar.com/passport/login.jsp?ret=https%3A%2F%2Fwww.qunar.com%2F"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.find_element(By.XPATH,"//*[text()='密码登录']").click()
driver.find_element(By.ID,'username').send_keys('13926033623')
driver.find_element(By.ID,'password').send_keys('lzh123456')
driver.find_element(By.ID,'agreement').click()
driver.find_element(By.XPATH,"//*[@id='app']/div/div[2]/div/div[1]/div[3]/div/div[3]").click()

action = ActionChains(driver)
action.click_and_hold(driver.find_element(By.XPATH,"//*[@id='app']/div/div[2]/div/div[1]/div[3]/div/div[5]/div/div/div[3]/div[3]"))
action.move_by_offset(500,0)
time.sleep(5)
action.release()
action.perform()
time.sleep(3)
cookies = driver.get_cookies()
with open(os.path.join('cookies.txt'),mode='w') as f:
    f.write(json.dumps(cookies))
driver.quit()

