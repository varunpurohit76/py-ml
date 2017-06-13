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
		self.cls = -1
	
	def sp(self, att):
		data = self.data
		data_l = []
		data_r = []
		for i in range(0, len(data)):
			if(data[i][att] ==0 ):
				temp = data[i][:]
				temp.pop(att)
				data_l.append(temp)
			else:
				temp = data[i][:]
				temp.pop(att)
				data_r.append(temp)
		self.left = Node(data_l)
		self.right = Node(data_r)
	
	def check_class(self):
		data = self.data
		for i in range(0, len(data)-1):
			if(data[i][-1] != data[i+1][-1]):
				return False
		self.cls = data[0][-1]
		return True

	def cal_p_log_p(self, n):
		return (-1*n*math.log(n, 2))
	
	def cal_info_gain(self, data):
		class_0 = 0
		class_1 = 0
		en = 0
		for i in range(0, len(data)):
			if(data[i][-1]==0):
				class_0+=1
			else:
				class_1+=1
		if(class_0 == 0 or class_1 == 0):
			return en
		else:
			if(class_0):
				en=en+self.cal_p_log_p(class_0/(class_0+class_1))
			if(class_1):
				en=en+self.cal_p_log_p(class_1/(class_0+class_1))
			return en
			
	def cal_gain_att(self, att):
		data = self.data
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
		return (((att_class_0/(att_class_0+att_class_1))*self.cal_info_gain(att_class_0_data))+((att_class_1/(att_class_0+att_class_1))*self.cal_info_gain(att_class_1_data)))
		
	def cal_max_gain_att(self, data):
		entropy = self.cal_info_gain(data)
		max_gain = 0
		max_att = -1
		for i in range(0, len(data[0])-1):
			gain_attribute = entropy - self.cal_gain_att(i)
			if(gain_attribute > max_gain):
				max_gain = gain_attribute
				max_att = i
		return max_att
	
	def check_no_att(self):
		data = self.data
		if(len(data[0]) <= 1):
			self.majority_vote()
			return True
		else:
			return False
	
	def majority_vote(self):
		data = self.data
		class_0 = 0
		class_1 = 0
		for i in range(0, len(data)):
			if(data[i][-1] == 0):
				class_0+=1
			else:
				class_1+=1
		self.cls = 0 if class_0>class_1 else 1
			

class Tree:
	def __init__(self, data):
		self.root = Node(data)
		
	def print_tree(self, node, level):
		if(node == None):
			return
		print("---Level--- %d with class %d" % (level, node.cls))
		print(node.data)
		self.print_tree(node.left, level+1)
		self.print_tree(node.right, level+1)


def id3(node):
	if(node.check_class()):
		return
	else:
		if(not node.check_no_att()):
			split_att = node.cal_max_gain_att(node.data)
			node.sp(split_att)
			id3(node.left)
			id3(node.right)

data = [[0,0,0,0],
	[1,0,0,1],
	[0,0,0,0],
	[1,1,0,1],
	[0,1,1,0],
	[1,1,1,0]]

t = Tree(data)

id3(t.root)
print("decision tree")
t.print_tree(t.root, 0)