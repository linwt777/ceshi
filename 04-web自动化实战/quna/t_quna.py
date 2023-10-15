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
