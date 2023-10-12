# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/12 19:47
# @File:5拖拽.py
from appium import webdriver
from selenium.webdriver.common.by import By
import time

desired_caps = {}
# 系统
desired_caps['platformName'] = 'Android'
# 版本
desired_caps['platformVersion'] = '7.1'
# 当前测试设备名称
desired_caps['deviceName'] = '127.0.0.1:62001'
# 要启动app的名称
desired_caps['appPackage'] = 'com.android.launcher3'
# 要启动的app的哪个页面
desired_caps['appActivity'] = '.launcher3.Launcher'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 拖拽
driver.drag_and_drop(driver.find_element(By.XPATH, "//*[@text='酷安']"),
                     driver.find_element(By.XPATH, "//*[@text='肯德基']"))

time.sleep(3)

# 关闭app
driver.close_app()
# 释放资源
driver.quit()
