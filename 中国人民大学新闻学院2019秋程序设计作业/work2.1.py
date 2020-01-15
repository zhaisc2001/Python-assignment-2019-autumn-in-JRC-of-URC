# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:08:05 2019

@author: ruanxinyu
"""
import csv,jieba.analyse,re#为了清洗数据，我们使用正则表达式
import matplotlib.pyplot as plt

# def get_chinese_font():#在matplotlib中添加字例
#     return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')
filename = '/Users/Violet/Documents/weibo_demolines.csv'
#文本在Windows系统下GB码解码中文会变成乱码，因此使用utf-8解码，使用‘rt’模式打开文件
with open(filename, mode='rt',encoding="utf-8") as f:
    reader = csv.reader(f)
    topics = []#将每条微博确立的话题（三个）按顺序存入列表
    def find_chinese(weibo):#由于爬取的微博内容是未清洗数据，我们这里对它进行清洗处理，使用正则表达式
        pattern = re.compile(r'[^\u4e00-\u9fa5]')
        chinese = re.sub(pattern, '', weibo)
        return chinese
#       print(chinese)
#制作微博文本热词
    def weiboTopic(weibo):
        keywords = jieba.analyse.extract_tags(weibo, topK=3, withWeight=False, allowPOS=())
        return keywords
    for row in reader:
        data = find_chinese(row[10])
        topics += weiboTopic(data)
    uni_topics = set(topics) #使用set将列表集合化，集合中的元素具有唯一性
    times_topics = [] #统计关键词出现频率，存入该列表
    for i in uni_topics:
        times_topics.append(topics.count(i))
    d = dict(zip(uni_topics,times_topics))#将两个列表合并成为一个字典
    d2 = sorted(d.items(),key=lambda item: item[1], reverse=True) #对字典排序
#    print(d2)
    #制作柱状图
    name_list = []
    num_list = []
    for j in range(10):
        name_list.append(d2[j][0])
        num_list.append(d2[j][1])

    plt.rcParams['font.family']='Microsoft YaHei'
    plt.xlabel("话题出现频次")
    plt.ylabel("热词")
    plt.title("微博文本话题及其出现热度")
    plt.barh(range(len(num_list)), num_list,tick_label = name_list)
    plt.show()


# import matplotlib
# print(matplotlib.matplotlib_fname()) #将会获得matplotlib包所在文件夹
# from matplotlib.font_manager import _rebuild
# _rebuild()
# import matplotlib
# for i in matplotlib.font_manager.fontManager.ttflist:
#     print(i)