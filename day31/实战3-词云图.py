import jieba
from wordcloud import WordCloud
#读取数据
with open('华为笔记本.txt','r',encoding='utf-8') as file:
    s=file.read()
#分词
lst=jieba.lcut(s)
#排除词
stopword=['散热性能','外形外观','轻薄程度','其他特色','屏幕效果']

txt=''.join(lst)
#绘制词云图
wordcloud = WordCloud(background_color='white',font_path='msyh.ttc',stopwords=stopword,width=800,height=600)

wordcloud.generate(txt)

wordcloud.to_file('华为笔记本评价词云图.png')