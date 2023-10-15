# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/15 17:28
# @File:book_order.py
from quna_po.base.base import Base
import time

class BookOrder(Base):

    def book_name(self):
        return self.byname('pName_0')

    def book_id(self):
        return self.byname('pCertNo_0')

    def book_order(self,name,id):
        self.book_name().send_keys(name)
        self.book_id().send_keys(id)
        time.sleep(2)