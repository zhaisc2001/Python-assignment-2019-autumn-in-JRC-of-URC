#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 23:23:43 2019

@author: ruanxinyu
"""

from snownlp import SnowNLP
#一、单篇微博
#（一）单篇微博的情感分析
#1.微博内容
weibo = u"""一生不长说短不短，不管人生处于哪个阶段，都应该少点执着，都需要学会时不时放空自己。
其实很多想不明白的事情，会在时间的推移下变得不是那样的重要，变得无所谓。放自己一马，让心真正休息，一步步学会放空的智慧，让生命微笑说放松。真好！"""

#2.单句情感分析
s = SnowNLP(weibo)

for sentence in s.sentences:
    print (sentence),
    score=str(SnowNLP(sentence).sentiments)
    print('Sentiment=' + score) 
#通过对单句情感得分的分析，我们认为0.3以下为消极情绪，0.3-0.65为中立情绪，0.65以上为积极情绪
#    if score>str(0.65):
#        print('Sentiment：Postive')
#    elif score<str(0.3):
#        print('Sentiment：Negative')
#    else:
#        print('Sentiment：Neutral')

#3.整篇文本情感分析

print(50*'-')
def weiboSentiment(weibo):
    a=[]#建立一个用于集合所有句子情感指数的空列表
#    x=0#positive的句子频数
#    y=0#negative的句子频数
#    z=0#neutral的句子频数
    for sentence in s.sentences:
        print (sentence),#print后面加逗号是和下一个print合到一行里
        score=str(SnowNLP(sentence).sentiments)
        print('Sentiment=' + score) 
        a.append(float(score))#把所有情感指数放入空列表中
    sent_score = sum(a)/len(a)#求情感得分的平均值
    print('语段情感得分为',sent_score)
    
#语段平均得分的if判断（已知得分为0-1之间的数）
    if 0 < sent_score <= 0.3:
        sent = 'Negative'
    elif 0.3 < sent_score <= 0.65:
        sent = 'Neutral'
    else:
        sent = 'Positive'
#    print(a)
#    for n in a:
#        if n>str(0.7):
#            x+=1
#        if n<str(0.3):
#            y+=1
#        if str(0.3)<=n<=str(0.7):
#            z+=1
#    print('Positive sentence:'+str(x))
#    print('Negative sentence:'+str(y))
#    print('Neutral sentence:'+str(z))
#    if x>y:
#        if x>z:
#            sent='Positive'
#        else:
#            sent='Neutral'
#    else:
#        if y>z:
#            sent='Negative'
#        else:
#            sent='Neutral'
    return '该篇微博的情感倾向：'+sent
    
print(weiboSentiment(weibo))
print(50*'=')

#（二）单篇微博的主题分析
#我们使用tf-idf方法，并通过jieba实现
import jieba.analyse

#1.分词
#设定关键词为三个，选出话题，关于jieba中的analyse方法介绍如下：
#jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=())
#	sentence 为待提取的文本
#	topK 为返回几个 TF/IDF 权重最大的关键词，默认值为 20
#	withWeight 为是否一并返回关键词权重值，默认值为 False
#	allowPOS 仅包括指定词性的词，默认值为空，即不筛选
#写成函数weiboTopic,方便之后多篇微博时调用
def weiboTopic(weibo):
    keywords = jieba.analyse.extract_tags(weibo, topK=3, withWeight=False, allowPOS=())
    return keywords
keyword = weiboTopic(weibo)
print(keyword)
##2.加载停用词文件
##filePath='/Users/ruanxinyu/Desktop/stopwords-master/哈工大停用词表.txt'
#
##inFile=open(filePath,'r')
##stopwords=inFile.read()
#
#words_no_stop = [] 
## 3.去除停用词
#for term in words:
#    if term not in stopwords:
#        words_no_stop.append(term)
#print(words_no_stop)    
#print(50*'-')
#for item in words_no_stop:
#    print(item)