# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/9 22:58
# @File:07键盘操作.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time

driver = webdriver.Chrome()

driver.get("https://baidu.com")  # 控制浏览器，访问百度

select = Select(driver.find_element(By.ID,"select"))
select.select_by_index(3)

select.select_by_value("bj")

select.select_by_visible_text("12")

driver.quit()  # 关闭浏览器
