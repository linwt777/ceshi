# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/16 10:26
# @File:test_unit_02.py
import unittest



class NumberTest(unittest.TestCase):
    def test_even(self):

        for i in range(0,6):
            with self.subTest(i=i):
                self.assertEqual(i % 2,0)