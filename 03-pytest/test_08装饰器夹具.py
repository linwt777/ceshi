# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/13 22:13
# @File:test_08装饰器夹具.py
import pytest

@pytest.fixture()
def before():
    print('before')

@pytest.fixture()
def login():
    print('login')
    return 'user'

@pytest.mark.usefixtures("before")
def test_1():
    print('test1')

def test_2(login):
    print('test2',login)

@pytest.fixture(params=[1,2,3])
def init_data(request):
    print("request参数是",request.param)
    return request.param

def test_Data(init_data):
    assert init_data>2