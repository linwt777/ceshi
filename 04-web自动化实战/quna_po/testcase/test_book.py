# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/15 17:30
# @File:test_book.py
from selenium.webdriver.chrome.webdriver import WebDriver

from quna_po.po.book_ticket_page import BookTicket
from quna_po.po.book_list import BookList
from quna_po.po.book_order import BookOrder
from selenium import webdriver
from quna_po.common.function import read_excel,date_n
import pytest
data = read_excel('../data/data.xlsx',0,True)

class Test_Book():


    def setup(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        url = "https://train.qunar.com/"
        self.driver.get(url)
        self.driver.maximize_window()

    @pytest.mark.parametrize(["start", "end", "n", "name", "id"], data)
    def test_01(self,start,end,n,name,id):
        ticket = BookTicket(self.driver)
        ticket.book_ticket(start,end,date_n(n))

        list = BookList(self.driver)
        list.book_list()

        order = BookOrder(self.driver)
        order.book_order(name,id)

    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main()