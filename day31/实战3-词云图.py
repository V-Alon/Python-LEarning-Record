import jieba
from wordcloud import WordCloud
#读取数据
with open('华为笔记本.txt','r',encoding='utf-8') as file:
    s=file.read()
#分词
lst=jieba.lcut
#排除词
stopword=['','','','','']