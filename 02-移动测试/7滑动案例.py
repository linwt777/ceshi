# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/12 19:28
# @File:4模拟手势.py
# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/10 22:51
# @File:1入门案例.py

# coding=utf-8

from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import time
desired_caps = {}
#系统
desired_caps['platformName'] = 'Android'
#版本
desired_caps['platformVersion'] = '7.1'
#当前测试设备名称
desired_caps['deviceName'] = '127.0.0.1:62001'
#要启动app的名称
desired_caps['appPackage'] = 'com.android.settings'
#要启动的app的哪个页面
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

action = TouchAction(driver)
el1 = driver.find_element(By.XPATH,"//*[@text='通知']")
el2 = driver.find_element(By.XPATH,"//*[@text='WLAN']")
action.press(el1).wait(0).move_to(el2).release().perform()

driver.find_element(By.XPATH,"//*[@text='安全']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@text='屏幕锁定']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@text='图案']").click()
time.sleep(3)

action.press(x=104,y=450).wait(0).move_to(x=436,y=453).wait().move_to(x=108,y=777).wait().move_to(x=434,y=780).release().perform()
time.sleep(3)
#关闭app
driver.close_app()
#释放资源
driver.quit()