# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/12 23:08
# @File:9真机实测.py
from appium import webdriver
from selenium.webdriver.common.by import By
import time
from appium.webdriver.common.touch_action import TouchAction
desired_caps = {}
#系统
desired_caps['platformName'] = 'Android'
#版本
desired_caps['platformVersion'] = '12.0'
#当前测试设备名称
desired_caps['deviceName'] = 'GE79TWVGZTE6BAA6'
#要启动app的名称
desired_caps['appPackage'] = 'com.miui.home'
#要启动的app的哪个页面
desired_caps['appActivity'] = 'com.miui.home.launcher.Launcher'

class caozuo():
#     # 卸载操作
    def xiezai(self):
        driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# action = TouchAction(driver)
# action.long_press(driver.find_element(By.XPATH,"//*[@text='']")).wait(5000).release()
# action.press()
# time.sleep(5)
# driver.close_app()
# driver.quit()
        driver.remove_app(r"melandru.lonicera")


c = caozuo()
c.xiezai()

