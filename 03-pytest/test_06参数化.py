# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/13 22:13
# @File:test_06参数化.py
import pytest

@pytest.mark.parametrize(['a','b'],[(1,2),(10,20),(30,40),(50,60),(70,80),(90,100),(110,120),(130,140)])
def test_a(a,b):
    print("test_a+++++++")
    assert a + b > 100


if __name__ == '__main__':
    pytest.main(["-s"])