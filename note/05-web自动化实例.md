## 1.数据驱动（python操作文件）

![image-20231014154054387](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231014154054387.png)

![image-20231014155001234](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231014155001234.png)

#### 1.1.txt文本操作

```
f= open("aaa.txt",mode='r',encoding="UTF8")

# print(f.readline())
#
# print(f.read())

print(f.readlines())
```

#### 1.2.csv文件操作

![image-20231014155041481](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231014155041481.png)

![image-20231014155503581](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231014155503581.png)

```
import csv
c = csv.reader(open("aaa.csv","r",encoding="utf-8"))
for cs in c :
    print(cs)
```

#### 1.3.excel文件

![image-20231014155930688](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231014155930688.png)

![image-20231014160326995](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231014160326995.png)

![image-20231014160353838](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231014160353838.png)

```
import xlrd

xls = xlrd.open_workbook("aaa.xlsx")

sheet = xls.sheet_by_index(0)
#获取行数
print(sheet.nrows)
#获取列数
print(sheet.ncols)

for i in range(sheet.nrows):
    print(sheet.row_values(i))
```

#### 1.4.Json操作

![image-20231014161345037](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231014161345037.png)

![image-20231014162845026](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231014162845026.png)

![image-20231014161420391](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231014161420391.png)

```
json_str = open("aaa.json","r",encoding="utf8").read()
print(json_str)

import json
#转成list格式
json_ob = json.loads(json_str)
print(json_ob)
print(type(json_ob))
print(json_ob[1][0]["name"])
print('------------')
#转回str
json2 = json.dumps(json_ob)
print(type(json2))
print(json.dumps(json2))
```

#### 1.5.xml文件操作

![image-20231014162501731](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231014162501731.png)

 ![image-20231014162905633](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231014162905633.png)

 ![image-20231014163005779](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231014163005779.png)

```
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

tree = ET.parse("aaa.xml")
root = tree.getroot()
print(root.tag)
print(root.attrib)
print(root.text)

for chlid in root:
    print(chlid.tag)
    print(chlid.attrib)
    print(chlid.text)
    for children in chlid:
        print(children.tag)
        print(children.text)
```

1.6.YAML文件操作

![image-20231014163953194](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231014163953194.png)

![image-20231014164418299](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231014164418299.png)

![image-20231014164444917](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231014164444917.png)

![image-20231014164517848](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231014164517848.png)

```
import yaml
# yaml_str = "animal: pets"

yaml_str = open("aaa.yaml","r",encoding="utf8").read()

yaml_ob = yaml.load(yaml_str,Loader = yaml.FullLoader)
print(yaml_ob)
```



## 2.实例

### 2.1测试用例设计

#### 使用去哪儿网

![image-20231015102245718](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231015102245718.png)

![image-20231015102333187](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231015102333187.png)

![image-20231015102227278](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231015102227278.png)

![image-20231015102400851](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231015102400851.png)

![image-20231014165145153](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231014165145153.png)

![image-20231015160708959](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231015160708959.png)

#### 基础层

```
# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/15 15:53
# @File:base_functions.py
from selenium import webdriver
import xlrd
from datetime import date,datetime,timedelta
import time,json
def date_n(n):
    return str(date.today()+timedelta(days = int(n)))

driver = webdriver.Chrome()

def get_driver():
    return driver

def open_url(url):
    driver.get(url)
    driver.maximize_window()

def close():
    driver.close()

#ishead是否有标题，由true，没有flase
def read_excel(filaname,index,ishead = False):
    xlsx = xlrd.open_workbook(filaname)
    sheet = xlsx.sheet_by_index(index)

    data=[]
    for i in range(sheet.nrows):
        if i == 0:
            if ishead:
                continue
        data.append(sheet.row_values(i))
    return data


# if __name__ == '__main__':
#     print(read_excel('data.xlsx', 0, True))
```

#### 业务代码层

```
# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/15 15:53
# @File:quna_book.py
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import date,datetime,timedelta
from quna.base_functions import *

def book_ticket(start,end,n,name,id):
    driver = get_driver()
    url = "https://train.qunar.com/"
    open_url(url)
    time.sleep(2)
    action = ActionChains(driver)
    # 设置出发到达日期；
    # 输入出发站，再点一下
    driver.find_element(By.NAME, 'fromStation').clear()
    driver.find_element(By.NAME, 'fromStation').send_keys(start)
    action.move_by_offset(0, 0)
    action.click()
    action.perform()

    driver.find_element(By.NAME, 'toStation').clear()
    driver.find_element(By.NAME, 'toStation').send_keys(end)
    action.move_by_offset(0, 0)
    action.click()
    action.perform()

    date_1 = date_n(n)
    # 删除之前日期，再输入
    # for i in "2023-10-17":
    #     driver.find_element(By.NAME,'date').send_keys(Keys.BACKSPACE)
    driver.find_element(By.NAME, 'date').send_keys(Keys.CONTROL, 'a')
    driver.find_element(By.NAME, 'date').send_keys(Keys.BACKSPACE)
    driver.find_element(By.NAME, 'date').send_keys(date_1)
    action.move_by_offset(0, 0)
    action.click()
    action.perform()
    driver.find_element(By.NAME, 'stsSearch').click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="list_listInfo"]/ul[2]/li[1]/div/div[7]/a[1]/span').click()
    driver.implicitly_wait(5)
    # 输入乘客信息
    driver.find_element(By.NAME, 'pName_0').send_keys(name)
    driver.find_element(By.NAME, 'pCertNo_0').send_keys(id)

    time.sleep(5)
    # close()
```

#### 测试代码层

```
# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/15 15:53
# @File:t_quna.py
from quna.quna_book import  book_ticket
from quna.base_functions import  read_excel
import pytest

data = read_excel("data.xlsx",0,True)

@pytest.mark.parametrize(["start","end","n","name","id"],data)
def test_book_ticket(start,end,n,name,id):
    # start = '北京'
    # end = '上海'
    # n = 2
    # name = '林'
    # id = '445221200106215911'
    book_ticket(start,end,n,name,id)


if __name__ == '__main__':
    pytest.main()
```



### po模式

![image-20231015163513702](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231015163513702.png)