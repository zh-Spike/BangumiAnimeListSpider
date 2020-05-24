# coding=utf-8
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
summarys = []
with open('BGM_jiandu_v2.csv', mode='r', encoding='utf-8') as f:
    rows = f.readlines()[0:251]
    for row in rows:
        summary = row.split(',')
        if summarys != '':
            summarys.append(summary)

jieba.add_word('汤浅政明')
jieba.add_word('渡边信一郎')
jieba.add_word('水岛精二')
jieba.add_word('石原立也')
jieba.add_word('水岛努')
jieba.add_word('今石洋之')
jieba.add_word('新房昭之')
jieba.add_word('佐藤大')
jieba.add_word('鹤卷和哉')
jieba.add_word('川面真也')
jieba.add_word('宫本茂')


comment_after_split = jieba.cut(str(summarys))
words = " ".join(comment_after_split)  # 以空格进行拼接

stopwords = STOPWORDS.copy()


bg_image = plt.imread('mioseng.jpg')

wc = WordCloud(width=1920, height=1080, background_color='white', mask=bg_image,
               font_path='STKAITI.TTF', stopwords=stopwords, max_font_size=300, random_state=50)
wc.generate_from_text(words)
plt.imshow(wc)
plt.axis('off')  # 不显示坐标轴c
plt.show()
# 保存结果到本地

wc.to_file('director.jpg')
