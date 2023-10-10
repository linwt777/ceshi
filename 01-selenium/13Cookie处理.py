# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/10 16:52
# @File:13Cookie处理.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://baidu.com")  # 控制浏览器，访问百度
driver.maximize_window()

time.sleep(5)
driver.add_cookie({"name":'BDUSS',"value":'XlTdGhOcXppUTNTR3VQMHctWFNLT2RiLVpsejNHOEtCb1FSclFGR3NTUXdua3hsRVFBQUFBJCQAAAAAAAAAAAEAAABc781Ezt610LqjzeK088rlMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADARJWUwESVlS'})
driver.add_cookie({"name":'BAIDUID',"value":'72F4970D7472E48031367678516D12F3:FG=1; BA_HECTOR=042l2lahag258gak00000k2h1iia0ii1o; ZFY=RzB3Um89aU5QcjUQgtIBEQt9:BegRWkCDTpWrBGOcOBc:C'})

time.sleep(5)
driver.refresh()

time.sleep(3)
driver.quit()  # 关闭浏览器
