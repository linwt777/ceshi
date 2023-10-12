# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/12 19:47
# @File:5拖拽.py
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import time

desired_caps = {}
# 系统
desired_caps['platformName'] = 'Android'
# 版本
desired_caps['platformVersion'] = '7.1'
# 当前测试设备名称
desired_caps['deviceName'] = '127.0.0.1:62001'
#要启动app的名称
desired_caps['appPackage'] = 'com.android.settings'
#要启动的app的哪个页面
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
el1 = driver.find_element(By.XPATH,"//*[@text='显示']")
el2 = driver.find_element(By.XPATH,"//*[@text='WLAN']")
#实例化TouchAction
action = TouchAction(driver)
#press既可以使用坐标，也可以使用元素,perform执行,在移动过程中，wait必不可少
action.press(el1).wait(500).move_to(el2).release().perform()

# 关闭app
driver.close_app()
# 释放资源
driver.quit()
