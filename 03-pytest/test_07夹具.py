# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/13 22:13
# @File:test_04测试.py
import pytest

def setup_module(args):
    print("setup_moudle",args)

def teardown_module(args):
    print("teardown_moudle",args)

def test_a():
    print('---','test-a')

def test_b():
    print('---','test-b')

class TestOne():
    TAG = 'A'
    def test_1(self):
        print('---',self.TAG, 'test-1')

    def test_2(self):
        print('---',self.TAG, 'test-2')