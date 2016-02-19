#! /usr/bin/python3
# -*- coding:utf8 -*-

"""
在管理实例方面，类装饰器如何与元类重叠？

答：两者都是在class语句的末尾自动触发，都可用于管理类实例。
    装饰器把类名重新绑定到一个可调用对象，元类则需要更多的操作来实现相同效果。
"""