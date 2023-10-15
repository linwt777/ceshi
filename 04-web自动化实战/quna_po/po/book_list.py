# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/15 17:26
# @File:book_list.py
import time

from quna_po.base.base import Base
class BookList(Base):
    def book_buy(self):
        return self.byxpath('//*[@id="list_listInfo"]/ul[2]/li[1]/div/div[7]/a[1]/span')

    def book_list(self):
        self.book_buy().click()
        time.sleep(2)