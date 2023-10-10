# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/9 22:58
# @File:07键盘操作.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()

driver.get("https://baidu.com")  # 控制浏览器，访问百度
# 根据id查询
el = driver.find_element(By.ID, 'kw')

#输入python
el.send_keys("python")
#全选
el.send_keys(Keys.CONTROL,"a")
time.sleep(2)
#删除
el.send_keys(Keys.BACK_SPACE)
time.sleep(2)
#输入美女
el.send_keys("美女")
time.sleep(2)
#全选
el.send_keys(Keys.CONTROL,"a")
time.sleep(2)
#复制
el.send_keys(Keys.CONTROL,"c")
time.sleep(2)
#删除
el.send_keys(Keys.BACK_SPACE)
time.sleep(2)
#粘贴
el.send_keys(Keys.CONTROL,"v")
time.sleep(5)
driver.quit()  # 关闭浏览器
