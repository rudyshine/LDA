import pandas as pd #加载pandas
from snownlp import SnowNLP


text=pd.read_csv(u'good.csv',header=0) #读取文本数据
text0=text.iloc[:,0] #提取所有数据
text1=[i for i in text0] #上一步提取数据不是字符而是object，所以在这一步进行转码为字符



senti=[SnowNLP(i).sentiments for i in text1] #遍历每条评论进行预测
newsenti=[]
for i in senti:
  if (i>=0.6):
      newsenti.append(1)
  else:
      newsenti.append(-1)
text['predict']=newsenti  #将新的预测标签增加为text的某一列，所以现在text的第0列为评论文本，第1列为实际标签，第2列为预测标签

counts=0
for j in range(len(text.iloc[:,0])): #遍历所有标签，将预测标签和实际标签进行比较，相同则判断正确。
    if text.iloc[j,2]==text.iloc[j,1]:
        counts+=1
print(u"准确率为:%f"%(float(counts)/float(len(text))))#输出本次预测的准确率