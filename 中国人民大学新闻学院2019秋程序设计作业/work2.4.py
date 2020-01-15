import csv,re,jieba.analyse
from wordcloud import WordCloud

filename = '/Users/Violet/Documents/秋季程序设计作业/multi_weibo.csv'

def weiboTopic(weibo):
    keywords=jieba.analyse.extract_tags(weibo, topK=30, withWeight=False, allowPOS=())
    return keywords

def find_chinese(weibo):  # 由于爬取的微博内容是未清洗数据，我们这里对它进行清洗处理，使用正则表达式
    pattern=re.compile(r'[^\u4e00-\u9fa5]')
    chinese=re.sub(pattern, '', weibo)

    return chinese
with open(filename, mode='rt',encoding="utf-8") as f:
    name = input('输入需要查询所有微博内容的用户名：')
    print('-'*50)
    content = ''
    reader = csv.reader(f)
    for row in reader:
        if(row[5] == name):content += find_chinese(row[9])

    topic = weiboTopic(content)
    text = ''
    for i in topic:text += i + ' '

    wc = WordCloud(    background_color="white", #背景颜色
                   max_words=200, #显示最大词数
                   font_path='/System/Library/Fonts/STHeiti Light.ttc'    )
    cloud_text = text
    wc.generate(cloud_text)
    wc.to_file("pic2.png")
