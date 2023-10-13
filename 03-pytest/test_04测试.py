# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/13 22:13
# @File:test_04测试.py
import pytest
def test_a():
    print("test_a")
    assert 1==1

def test_b():
    print("test_b")
    assert "a" in "hellp"

if __name__ == '__main__':
    pytest.main(["-s","test_04测试.py"])