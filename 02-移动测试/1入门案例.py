# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/10 22:51
# @File:1入门案例.py

# coding=utf-8

from appium import webdriver
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

time.sleep(10)
#关闭app
driver.close_app()
#释放资源
driver.quit()