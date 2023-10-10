### ![image-20231008230146969](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231008230146969.png)

![image-20231008230223569](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231008230223569.png)

需要下载驱动

使用selenium

```
from selenium import webdriver

driver = webdriver.Chrome() #启动浏览器
driver.get("https://baidu.com") #控制浏览器，访问百度

driver.quit() #关闭浏览器
```



### 1.元素定位

```
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://baidu.com")  # 控制浏览器，访问百度
# 根据id查询
# driver.find_element(By.ID, 'kw').send_keys("美女")
# driver.find_element(By.ID, 'su').click()
#
# # 根据name查询
# driver.find_element(By.NAME, 'wd').send_keys("美女")
# driver.find_element(By.ID, 'su').click()
# #根据classname查找
# driver.find_element(By.CLASS_NAME,"s_ipt").send_keys("美女")
# driver.find_element(By.ID, 'su').click()

#根据a标签查询
# driver.find_element(By.LINK_TEXT,"hao123").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"hao12").click()

#css选择器定位
# driver.find_element(By.CSS_SELECTOR,"#su").click()
# time.sleep(5)

driver.quit()  # 关闭浏览器

```



Xpath元素定位

![image-20231009212908908](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231009212908908.png)

```
driver.find_element(By.XPATH,"//*[@id='kw']").send_keys("第一次")
driver.find_element(By.XPATH,"//*[@id='su']").click()
```



### 2.浏览器操作

![image-20231009214440389](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231009214440389.png)

```
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = "https://baidu.com"

driver.get(url)

#最大化浏览器
driver.maximize_window()
#设置浏览器宽高
driver.set_window_size(980,1080)
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='kw']").send_keys("123")
driver.find_element(By.XPATH,"//*[@id='su']").click()
time.sleep(2)
#浏览器后退
driver.back()
time.sleep(2)
#浏览器前进
driver.forward()
time.sleep(2)
#刷新浏览器
driver.refresh()
time.sleep(2)
driver.back()
driver.find_element(By.XPATH,"//*[text()='hao123']").click()
time.sleep(2)
#关闭当前页面
driver.close()

time.sleep(3)
driver.quit()
```

### 3.页面等待

```
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # 新增
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()


driver.get("https://baidu.com") #控制浏览器，访问百度

driver.find_element(By.ID, 'kw').send_keys("美女")
driver.find_element(By.ID, 'su').click()

#进行页面等待
#3种 强制，显式，隐式
#强制
# time.sleep(3)

#显式
#等待某个元素加载完成，每隔0.5秒加载一次，最多加载5秒
# WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"//*[@class='image-content_1csSY']")))

#隐式
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//*[@class='image-content_1csSY']").click()

time.sleep(2)

driver.quit() #关闭浏览器
```

显式等待表明了具体等待某个元素，隐式等待则没有



### 5.元素操作

![image-20231009223443637](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231009223443637.png)

```
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://baidu.com")  # 控制浏览器，访问百度


#xpath定位
# driver.find_element(By.XPATH,"//*[@id='kw']").send_keys("第一次")
# #清楚输入文字
# driver.find_element(By.XPATH,"//*[@id='kw']").clear()
#
# driver.find_element(By.XPATH,"//*[@id='kw']").send_keys("python")
# driver.find_element(By.XPATH,"//*[@id='su']").click()

print(driver.find_element(By.XPATH, "//*[@id='kw']").size)
print(driver.find_element(By.XPATH, "//*[@id='kw']").text)
print(driver.find_element(By.XPATH, "//*[@id='kw']").is_enabled())
print(driver.find_element(By.XPATH, "//*[@id='kw']").is_displayed())

print(driver.find_element(By.XPATH, "//*[text()='新闻']").get_attribute('href'))

time.sleep(5)
driver.quit()  # 关闭浏览器
```



### 6.模拟鼠标操作

![image-20231009224224618](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231009224224618.png)



```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://baidu.com")  # 控制浏览器，访问百度
action =ActionChains(driver)
#点击右键
# action.context_click(driver.find_element(By.XPATH,"//*[@id='su']"))

#悬停
# action.move_to_element(driver.find_element(By.XPATH,"//*[@class='soutu-btn']"))
# action.perform()

#拖拽
# action.drag_and_drop(driver.find_element(By.ID,'div1'),driver.find_element(By.ID,'div2'))

time.sleep(5)
driver.quit()  # 关闭浏览器
```



### 7.模拟键盘操作

![image-20231009225728004](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231009225728004.png)



```
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
```

### 8.下拉框选择

![image-20231009230637607](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231009230637607.png)

```
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
```



### 9.页面滚动

![image-20231010152221134](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231010152221134.png)

```
# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/9 15:33
# @File:02元素定位.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.douyu.com/directory/all")  # 控制浏览器，访问百度
driver.maximize_window()

#selenuim中并没有页面滚动，使用js代码
js_str='window.scrollTo(0,10000)'

driver.execute_script(js_str)

time.sleep(5)
driver.find_element(By.XPATH,"//*[text()='下一页']").click()

time.sleep(5)
driver.quit()  # 关闭浏览器

```



### 10.警告框处理

![image-20231010154823005](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231010154823005.png)

### 11.frame切换

![image-20231010161158699](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231010161158699.png)

```
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://mail.qq.com")  # 控制浏览器，访问百度
driver.maximize_window()
driver.switch_to.frame(driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[1]/div/div[2]/div[2]/iframe"))

time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div[1]/div[10]/a[1]']").click()

time.sleep(3)
driver.find_element(By.XPATH,"//*[@id="u"]").send_keys("123456")

#返回原始页面
driver.switch_to.default_content()
time.sleep(3)
driver.quit()  # 关闭浏览器
```



### 12.页面切换

![image-20231010163634386](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231010163634386.png)

```
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://baidu.com")  # 控制浏览器，访问百度
driver.maximize_window()

print(driver.window_handles)
print(driver.current_window_handle)

driver.find_element(By.ID, 'kw').send_keys("美女")
driver.find_element(By.ID, 'su').click()

driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//*[@class='image-content_1csSY']").click()

print(driver.window_handles)
print(driver.current_window_handle)

#切换页面
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='srcPic']/img").click()

time.sleep(3)
driver.quit()  # 关闭浏览器
```

### 12.截图

![image-20231010164716524](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231010164716524.png)

```
driver.get_screenshot_as_file('1.png')
```



### 13.cookie的处理

![image-20231010164933804](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231010164933804.png)

```
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
```