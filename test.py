# -*- coding: utf-8 -*-
# 用于测试code的文件
L = [1,2,3,4]
if type(L) == type([]):
	print("L is list")
if type(L) == list:
	print("L is list")
if isinstance(L,list):
	print("L is list")
print "test"