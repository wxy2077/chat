#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 15:32
# @Author  : CoderCharm
# @File    : a_test.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

测试 Python 对象的存储还原。

https://stackoverflow.com/questions/15219858/how-to-store-a-complex-object-in-redis-using-redis-py

obj = ExampleObject()
pickled_object = pickle.dumps(obj)
r.set('some_key', pickled_object)
unpacked_object = pickle.loads(r.get('some_key'))
obj == unpacked_object


typing.Dict[key_type, value_type]

"""

# import pickle
#
#
# class Cat(object):
#     def __init__(self, z):
#         self.z = z
#
#
# a = Cat("121")
# # 输出对象id
# print("对象id", id(a))
#
# pickled_object = pickle.dumps(a)
#
# print("查看转换后的数据", pickled_object, type(pickled_object))
#
# unpacked_object = pickle.loads(pickled_object)
#
# print("还原后的数据", unpacked_object, id(unpacked_object))
#
# print("调用结果", unpacked_object.z)
#

