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