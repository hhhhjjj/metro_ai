from snownlp import SnowNLP
text = u"这个书包的质量不太好，我很生气"
s = SnowNLP(text)
print(",".join(s.words))
# 这个是分词，jieba的分词比这个要好

for data in s.keywords(2):
    # 这个2是提取关键词的个数
    print(data)

for sentence in s.sentences:
    # 拆分成句子，感觉就是根据标点符号分的。。
    print(sentence)

print(s.sentiments)
# 情感分析，积极的概率
# 我这都很生气了，积极概率还这么高。。
# 当然这个是可以通过训练来优化的
