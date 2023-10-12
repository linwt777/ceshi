# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/12 16:37
# @File:3基本操作.py
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

time.sleep(1)
#安装app
# driver.install_app(r"G:\Web-Test\selenium-test\Youku_11.0.48_19babfbcea8e1838.apk")
#卸载app
if driver.is_app_installed('com.youku.phone'):
    driver.remove_app('com.youku.phone')

#输入操作
driver.find_element(By.XPATH,"//*[@resource-id='com.android.settings:id/search']").click()


driver.find_element(By.XPATH,"//*[@resource-id='android:id/search_src_text']").send_keys("第一次")

time.sleep(2)
driver.find_element(By.XPATH,"//*[@resource-id='android:id/search_src_text']").clear()
#关闭app
driver.close_app()
#释放资源
driver.quit()