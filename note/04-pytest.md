

### 1.介绍

![image-20231013211641669](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231013211641669.png)

![image-20231013213036995](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231013213036995.png)

```
#单元测试 1.测试函数，类，方法能不能正确的运行完成
import pytest
def test_a():
    print(test_a)
    return 1 * 0

def test_b():
    print(test_b)
    return 1 / 0

if __name__ == '__main__':
    pytest.main(["-s"])
```

### 2.基本配置

![image-20231013213523412](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231013213523412.png)

![image-20231013215339544](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231013215339544.png)

### 3.断言

![image-20231013221156186](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231013221156186.png)

```
import pytest
def test_a():
    print("test_a")
    assert 1==1

def test_b():
    print("test_b")
    assert "a" in "hellp"

if __name__ == '__main__':
    pytest.main(["-s","test_04测试.py"])
```



### 4.标记

![image-20231013221725490](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231013221725490.png)

```
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
```



### 5.参数化

![image-20231013222501959](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231013222501959.png)

```
import pytest

@pytest.mark.parametrize(['a','b'],[(1,2),(10,20),(30,40),(50,60),(70,80),(90,100),(110,120),(130,140)])
def test_a(a,b):
    print("test_a+++++++")
    assert a + b > 100


if __name__ == '__main__':
    pytest.main(["-s"])
```

### 6.夹具

![image-20231013222955858](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231013222955858.png)

![image-20231013223434344](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231013223434344.png)

![image-20231013223504490](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231013223504490.png)

```
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
```



![image-20231013225021176](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231013225021176.png)

![image-20231013225142976](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231013225142976.png)

![image-20231013225305459](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231013225305459.png)

![image-20231013225556188](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231013225556188.png)

```
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
```



### 7.插件

![image-20231013230204103](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231013230204103.png)

```
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
```



![image-20231013231820987](C:\Users\林伟腾\AppData\Roaming\Typora\typora-user-images\image-20231013231820987.png)

完整代码再文件夹中