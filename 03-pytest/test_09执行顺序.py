# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/13 22:13
# @File:test_08装饰器夹具.py
import pytest
#标记了运行顺序的，正数越小先运行，标记了运行的优先级大于未标记的 则正整数>没有标记>负整数
@pytest.mark.run(order = 5)
def test_1():
    print('test1')
@pytest.mark.run(order = -3)
def test_2():
    print('test2')
@pytest.mark.run(order = 1)
def test_3():
    print('test3')
@pytest.mark.run(order = 2)
def test_4():
    print('test4')
@pytest.mark.run(order = 6)
def test_5():
    print('test5')
@pytest.mark.run(order = 4)
def test_6():
    print('test6')

