# -*- coding: utf-8 -*-
#-- 寻求帮助：
	# dir(obj)		# 简单的列出对象obj所包含的方法名称，返回一个字符串列表
	# help(obj.func) # 查询obj.func的具体介绍和用法
import os
dir(os)
help(os.mkdir)
#-- 测试类型的三种方法，推荐第三种
L = [1,2,3,4]
if type(L) == type([]):
	print("L is list")
if type(L) == list:
	print("L is list")
if isinstance(L,list):
	print("L is list")