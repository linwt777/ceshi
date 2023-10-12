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
#获取屏幕分辨率
size = driver.get_window_size()
width = size['width']
height = size['height']
#
# time.sleep(1)
#使用swper由点对点移动
# driver.swipe(start_x=270,start_y=640,end_x=270,end_y=320)
#scroll则是由一个元素移动到里一个元素
# driver.scroll(driver.find_element(By.XPATH,"//*[@text='显示']"),driver.find_element(By.XPATH,"//*[@text='WLAN']"))
time.sleep(2)

#关闭app
driver.close_app()
#释放资源
driver.quit()