# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/13 21:27
# @File:test_01测试.py
#单元测试 1.测试函数，类，方法能不能正确的运行完成
def test_a():
    print("test_a")
    return 1 * 0

def test_b():
    print("test_b")
    return 1 / 0

def demo_a():
    print("demo_a-------------------")
    return 1 * 0

def demo_b():
    print("demo_b----------")
    return 1 / 0

# if __name__ == '__main__':
#     pytest.main(["-s"])