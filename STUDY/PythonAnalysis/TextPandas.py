import pandas as pd

df=pd.read_csv('/home/390646/PycharmProjects/jdcrawl_v1.0/4521778jd_table.csv')
# print(df)

# #打印数据前五行
# print(df.head())

# #打印数据后5行
# print(df.tail())

# #打印列名
# print(df.columns)

# #打印行名
# print(df.index)

# #打印10~20行前三列数据
# print(df.ix[10:20, 0:3])

# #提取不连续行和列的数据，这个例子提取的是第1,3,5行，第2,4列的数据
# print(df.iloc[[1,3,5],[2,4]])

# #专门提取某一个数据，这个例子提取的是第三行，第1列数据（默认从0开始算哈,且不算标题行）
# print(df.iat[3,1])

# ##计数统计，example：统计userClient
# count = df['userClient'].value_counts()
# print(count)

##通过describe属性，对数据的统计特性进行描述
# print(df.describe())

##舍弃数据中的列数，舍弃第一列和第二列
# （axis 参数告诉函数到底舍弃列还是行。如果axis等于0，那么就舍弃行。）
print(df.drop(df.columns[[1, 2]], axis = 1).head())