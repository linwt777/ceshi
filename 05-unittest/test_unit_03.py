# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/16 10:49
# @File:test_unit_03.py
import unittest
from unittest import TextTestRunner
from test_unit_01 import TestOne
from unittest.loader import makeSuite
import HtmlTestRunner
# suite = unittest.TestSuite()

#单个
# suite.addTest(TestOne("test_01"))

#添加某个测试类多个方法
# suite.addTests(map(TestOne,["test_01","test_02"]))

#添加测试类所有方法
# suite.addTest(makeSuite(TestOne))
# runner = TextTestRunner()
#
# runner.run(suite)
test_dir = './'
suite = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

runner = HtmlTestRunner.runner.HTMLTestRunner()
runner.run(suite)

