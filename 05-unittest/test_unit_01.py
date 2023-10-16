# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/16 10:12
# @File:test_unit_01.py

import unittest

def setUpModule():
    print("setUpMoudle")

def tearDownModule():
    print("tearDownMoudle")

class TestOne(unittest.TestCase):
    def test_01(self):
        # response = '响应成功'
        # self.assertIn("0",response)
        response = '响应成功'
        self.assertIn("成功",response)
        print("123465")

    def test_02(self):
        print("test_02")


if __name__ == '__main__':
    unittest.main()
