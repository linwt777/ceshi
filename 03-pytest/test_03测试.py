# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/13 21:27
# @File:test_03测试.py
#单元测试 1.测试函数，类，方法能不能正确的运行完成

class TestOne():
    def test_3(self):
        print("test_3")
        return 1 * 0

    def test_4(self):
        print("test_4")
        return 1 / 0

# if __name__ == '__main__':
#     pytest.main(["-s","test_01测试.py"])