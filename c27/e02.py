#! /usr/bin/python3
# -*- coding:utf8 -*-

"""
当我们从一个shelve获取一个Person对象而没有导入其模块的时候，该对象如何知道它有一个giveRaise方法可供我们调用？

答：实例载入内存时，shelve（实际上使用的是pickle模块）会自动地把该实例重新连接到创建它的类。python从其模块内部重新导入该类，并把实例的__class__指向其最初的类。从而使得载入实例自动获取所有其他最初方法。
"""
