# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/13 22:13
# @File:test_05断言.py
import pytest
def test_a():
    print("test_1")
    return 1

@pytest.mark.skip(reason="我想跳过")
def test_b():
    print("test_2")
    return 1 / 0

@pytest.mark.xfail(raises=ZeroDivisionError)
def test_c():
    print("test_3")
    return 1 / 1

if __name__ == '__main__':
    pytest.main(["-s"])