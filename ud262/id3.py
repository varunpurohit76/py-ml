# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 23:38:22 2017

@author: Varun
"""

import math

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	def sp(self, att):
		data = self.data
		data_l = []
		data_r = []
		for i in range(0, len(data)):
			if(data[i][att] ==0 ):
				data_l.append(data[i])
			else:
				data_r.append(data[i])
		self.left = Node(data_l)
		self.right = Node(data_r)

class Tree:
	def __init__(self, data):
		self.root = Node(data)


def cal_p_log_p(n):
	return (-1*n*math.log(n, 2))

def cal_entropy(data):
	class_0 = 0
	class_1 = 0
	en = 0
	for i in range(0, len(data)):
		if(data[i][3]==0):
			class_0+=1
		else:
			class_1+=1
	if(class_0 == 0 or class_1 == 0):
		return en
	else:
		if(class_0):
			en=en+cal_p_log_p(class_0/(class_0+class_1))
		if(class_1):
			en=en+cal_p_log_p(class_1/(class_0+class_1))
		return en

def cal_gain(att):
	att_class_0 = 0
	att_class_0_data = []
	att_class_1 = 0
	att_class_1_data = []
	for i in range(0, len(data)):
		if(data[i][att]==0):
			att_class_0+=1
			att_class_0_data.append(data[i])
		else:
			att_class_1+=1
			att_class_1_data.append(data[i])
	print(((att_class_0/(att_class_0+att_class_1))*cal_entropy(att_class_0_data))+((att_class_1/(att_class_0+att_class_1))*cal_entropy(att_class_1_data)))

	
attribute_list = ["a", "b", "c", "target"]
data = [[0,0,0,0],
	[0,1,0,1],
	[0,0,0,0],
	[1,1,1,1],
	[1,0,1,0],
	[1,1,1,1]]
	
print(cal_entropy(data))
print("info gain for attribute 1")
cal_gain(0)
print("info gain for attribute 2")
cal_gain(1)
print("info gain for attribute 3")
cal_gain(2)

t = Tree(data)
print(t.root.data)
t.root.sp(1)
print("---")
print(t.root.left.data)
print("---")
print(t.root.right.data)