### 1.入门案例

![image-20231016100856282](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231016100856282.png)

![image-20231016101020591](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231016101020591.png)

![image-20231016101127323](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231016101127323.png)

```
import unittest


class TestOne(unittest.TestCase):
    def test_01(self):
        print("test_01")

    def test_02(self):
        print("test_02")


if __name__ == '__main__':
    unittest.main()
```



### 2.断言

![image-20231016101757999](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231016101757999.png)

![image-20231016101939763](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231016101939763.png)

![image-20231016101958598](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231016101958598.png)

```
import unittest


class TestOne(unittest.TestCase):
    def test_01(self):
        # response = '响应成功'
        # self.assertIn("0",response)
        response = '响应成功'
        self.assertIn("成功",response)

    def test_02(self):
        print("test_02")


if __name__ == '__main__':
    unittest.main()
```

### 3.子测试

![image-20231016102435623](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231016102435623.png)

### 4.fixture（夹具）

![image-20231016104142839](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231016104142839.png)

![image-20231016104428809](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231016104428809.png)

![image-20231016104641358](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231016104641358.png)

```
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

    def test_02(self):
        print("test_02")


if __name__ == '__main__':
    unittest.main()
```

### 4.TestSuite&TestRunner

![image-20231016104854982](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231016104854982.png)

![image-20231016104910532](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231016104910532.png)

![image-20231016105658018](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231016105658018.png)

```
# @File:test_unit_03.py
import unittest
from unittest import TextTestRunner
from test_unit_01 import TestOne
from unittest.loader import makeSuite

suite = unittest.TestSuite()

#单个
# suite.addTest(TestOne("test_01"))

#添加某个测试类多个方法
# suite.addTests(map(TestOne,["test_01","test_02"]))

#添加测试类所有方法
suite.addTest(makeSuite(TestOne))

runner = TextTestRunner()

runner.run(suite)
```

### 5.TestLoader&TestResult

![image-20231016105904998](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231016105904998.png)

![image-20231016105956074](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231016105956074.png)

```
test_dir = './'
suite = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

runner = HtmlTestRunner.runner.HTMLTestRunner()
runner.run(suite)
```