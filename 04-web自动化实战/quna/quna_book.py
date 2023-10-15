# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/15 15:53
# @File:quna_book.py
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import date,datetime,timedelta
from quna.base_functions import *

def book_ticket(start,end,n,name,id):
    driver = get_driver()
    url = "https://train.qunar.com/"
    open_url(url)
    time.sleep(2)
    action = ActionChains(driver)
    # 设置出发到达日期；
    # 输入出发站，再点一下
    driver.find_element(By.NAME, 'fromStation').clear()
    driver.find_element(By.NAME, 'fromStation').send_keys(start)
    action.move_by_offset(0, 0)
    action.click()
    action.perform()

    driver.find_element(By.NAME, 'toStation').clear()
    driver.find_element(By.NAME, 'toStation').send_keys(end)
    action.move_by_offset(0, 0)
    action.click()
    action.perform()

    date_1 = date_n(n)
    # 删除之前日期，再输入
    # for i in "2023-10-17":
    #     driver.find_element(By.NAME,'date').send_keys(Keys.BACKSPACE)
    driver.find_element(By.NAME, 'date').send_keys(Keys.CONTROL, 'a')
    driver.find_element(By.NAME, 'date').send_keys(Keys.BACKSPACE)
    driver.find_element(By.NAME, 'date').send_keys(date_1)
    action.move_by_offset(0, 0)
    action.click()
    action.perform()
    driver.find_element(By.NAME, 'stsSearch').click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="list_listInfo"]/ul[2]/li[1]/div/div[7]/a[1]/span').click()
    driver.implicitly_wait(5)
    # 输入乘客信息
    driver.find_element(By.NAME, 'pName_0').send_keys(name)
    driver.find_element(By.NAME, 'pCertNo_0').send_keys(id)

    time.sleep(5)
    # close()