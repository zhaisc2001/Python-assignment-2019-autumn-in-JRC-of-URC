# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 19:15:05 2019

@author: ruanxinyu
"""

import csv
import matplotlib.pyplot as plt
filename = '/Users/Violet/Documents/weibo_demolines.csv'
#文本在Windows系统下GB码解码中文会变成乱码，因此使用utf-8解码，使用‘rt’模式打开文件
with open(filename, mode='rt',encoding="utf-8") as f:
    reader = csv.reader(f)
#制作用户类型
    types = []
    for row in reader:
        types.append(row[8])
#    print(types)
    times_types = []
    for i in types:
        times_types.append(types.count(i))
    d3 = dict(zip(types,times_types))#将两个列表合并成为一个字典
    d3.pop('用户类型')#由于读取csv文件时读取了第一行，这里删去
    print(d3)
    d4 = sorted(d3.items(),key=lambda item: item[1], reverse=True) #对字典排序
    name_list = []
    num_list = []
    for j in d4:
        name_list.append(j[0])
        num_list.append(j[1])
    plt.rcParams['font.family']='Microsoft YaHei'
#绘制饼状图
    labels = name_list
    fracs = num_list
    plt.axes(aspect=1)
    plt.pie(x=fracs,labels=labels,autopct='%.0f%%')
    plt.title("微博用户类型")
    plt.show()  
