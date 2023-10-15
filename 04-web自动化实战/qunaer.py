# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/15 10:56
# @File:qunaer.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import date,datetime,timedelta
import time,json
def date_n(n):
    return str(date.today()+timedelta(days = int(n)))


url = "https://train.qunar.com/"
# with open(r'cookies.txt',mode='r') as f:
#     cookies_file = f.read()
# #将读取的文件转为json格式
# cookie_list = json.loads(cookies_file)
driver = webdriver.Chrome()
#低版本的selenuim可以封装看起来更简便，高版本看情况
# def name(element):
#     return driver.find_element(By.NAME,element)
#
# def xpath(element):
#     return driver.find_element(By.XPATH,element)

driver.get(url)
driver.maximize_window()
# driver.maximize_window()
# for cookie in cookie_list:
#     print(cookie)
#     driver.add_cookie(cookie)
action = ActionChains(driver)
#设置出发到达日期；
#输入出发站，再点一下
driver.find_element(By.NAME,'fromStation').send_keys('北京')
action.move_by_offset(0,0)
action.click()
action.perform()

driver.find_element(By.NAME,'toStation').send_keys('上海')
action.move_by_offset(0,0)
action.click()
action.perform()

date_1 = date_n(3)
#删除之前日期，再输入
# for i in "2023-10-17":
#     driver.find_element(By.NAME,'date').send_keys(Keys.BACKSPACE)
driver.find_element(By.NAME,'date').send_keys(Keys.CONTROL,'a')
driver.find_element(By.NAME,'date').send_keys(Keys.BACKSPACE)
driver.find_element(By.NAME,'date').send_keys(date_1)
action.move_by_offset(0,0)
action.click()
action.perform()
driver.find_element(By.NAME,'stsSearch').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="list_listInfo"]/ul[2]/li[1]/div/div[7]/a[1]/span').click()
driver.implicitly_wait(5)
#输入乘客信息
driver.find_element(By.NAME,'pName_0').send_keys('林伟腾')
driver.find_element(By.NAME,'pCertNo_0').send_keys('445221200106215911')

time.sleep(5)
driver.quit()

