# 题目：
# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
# def product(x, y):
#     return x * y

# -*- coding: utf-8 -*-
import math

def product(x, *y):
    for n in y:
        x *= n
    return x
# 这个应该是最好的一个解决办法：有必选参数，这样如果没输入会报错；有可变参数，这样得到一个tuple
# 并且最终回归值是x，省了行数。

# 测试：
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败！')
elif product(5,6) != 30:
    print('测试失败！')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
