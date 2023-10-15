# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/15 17:04
# @File:book_ticket_page.py.py
from selenium.webdriver.common.keys import Keys

from quna_po.base.base import Base
from selenium.webdriver.common.action_chains import ActionChains
import time

class BookTicket(Base):
    def move_click(self):
        action = ActionChains(self.driver)
        action.move_by_offset(0, 0)
        action.click()
        action.perform()

    def book_start(self):
        return self.byname('fromStation')

    def book_end(self):
        return self.byname('toStation')

    def book_date(self,date):
        self.byname('date').send_keys(Keys.CONTROL, 'a')
        self.byname('date').send_keys(Keys.BACKSPACE)
        self.byname('date').send_keys(date)

    def book_search(self):
        return self.byname('stsSearch')

    def book_ticket(self,start,end,date):
        url = "https://train.qunar.com/"
        self.open_url(url)
        time.sleep(2)
        self.move_click()
        # 设置出发到达日期；
        # 输入出发站，再点一下
        self.book_start().send_keys(start)
        self.move_click()

        self.book_end().send_keys(end)
        self.move_click()


        # 删除之前日期，再输入
        # for i in "2023-10-17":
        #     driver.find_element(By.NAME,'date').send_keys(Keys.BACKSPACE)
        self.book_date(date)
        self.move_click()

        #点击立即搜索
        self.book_search().click()

        time.sleep(2)