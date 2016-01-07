#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：继承搜索在哪里查找属性？
答：继承搜索首先在引发搜索操作的对象内部开始，如果该对象是个实例那就是先在实例对象中寻找属性，然后搜索创建该实例的类，之后是该类的超类等。按照继承搜索树从下到上，从左到右的顺序搜索。当属性首次找到时，搜索就会停止。
'''