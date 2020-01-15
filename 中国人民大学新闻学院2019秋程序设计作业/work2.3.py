# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 19:19:09 2019

@author: ruanxinyu
"""
import csv,jieba.analyse,re#为了清洗数据，我们使用正则表达式
from wordcloud import WordCloud 
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
    text = ''#将话题由列表转化为字符串，方便做成词云
    for i in topics:
        text += i + ' '
    print(text)
    wc = WordCloud(    background_color="white", #背景颜色    
                   max_words=200, #显示最大词数   
                   font_path='/System/Library/Fonts/STHeiti Light.ttc'    )
    cloud_text = text
    wc.generate(cloud_text)
    wc.to_file("pic2.png")
