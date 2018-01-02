# #-*-utf8-*-
# import pymongo
# from bs4 import BeautifulSoup
# from urllib import request
# import random
# url="https://sale.jd.com/act/GrZjoT7UQWCn.html"
# html=request.urlopen(url).read()
# soup=BeautifulSoup(html,"lxml")
# #
# for link in soup.find_all('a'):
#     print(link.get('href'))
#获取skuid
# client = pymongo.MongoClient('localhost', 27017)
# rent_info = client['jd_table_productId']  # 给数据库命名
# sheet_table = rent_info['jd_table_productId']  # 创建表单
# for skuid in soup.find_all('li'):
#     productId=skuid.get('skuid')
#     if productId!=None:
#         # print(productId)
#         # print(type(productId))
#         sheet_table.insert({'productId': productId,})
#         print("done......")
# db = pymongo.MongoClient().jd_table_productId
# # print(db)
# for i in db.jd_table_productId.find():
#     print(i)
#     productId=i.values()
#     print(productId)


# import pymongo
# from bs4 import BeautifulSoup
# from urllib import request
# import random
# url="https://sale.jd.com/act/GrZjoT7UQWCn.html"
# html=request.urlopen(url).read()
# soup=BeautifulSoup(html,"lxml")
# #
# for link in soup.find_all('a'):
#     print(link.get('href'))
##获取skuid
# from bs4 import BeautifulSoup
# from urllib import request
# import random
# url="https://sale.jd.com/act/GrZjoT7UQWCn.html"
# html=request.urlopen(url).read()
# soup=BeautifulSoup(html,"lxml")
# for skuid in soup.find_all('li'):
#     Id=skuid.get('skuid')
#     # Id = [skuid.get('skuid')]
#     if Id!=None:
#         # for i in range(0,len(Id)):
#         #     print(i,Id[i])
#
#         # for Id in Id:
#             # print(list(Id))
#         productId=''.join(Id)
#         print( type(productId))

        # print(Id)
        # i=1
        # for i in range(len(Id)):
        #     print(i,Id)



##获取skuid ,缺少一个循环
# import requests
# import re
# import codecs
# url0="https://sale.jd.com/act/GrZjoT7UQWCn.html"
# session = requests.session()
# website = session.get(url0)
# content=str(website.content)
# print (content)
# start = content.find('skuid') + 7
# end = content[start:].find('"') + start
# id = content[start:end]
# print("11111",start)
# print("22222",end)
# print(id)


#

# url="https://sale.jd.com/act/GrZjoT7UQWCn.html"
# html=request.urlopen(url).read()
# soup=BeautifulSoup(html,"lxml")
# for skuid in soup.find_all('li'):
#     Id=skuid.get('skuid')
#     if Id!=None:
#         productId=Id
#
#         print(productId)
##获取productId并将str lis 转换成list
# url="https://sale.jd.com/act/GrZjoT7UQWCn.html"
# html=request.urlopen(url).read()
# soup=BeautifulSoup(html,"lxml")
# for skuid in soup.find_all('li'):
#     Id=skuid.get('skuid')
#     if Id!=None:
#         Id=str.split(Id)
#         for i in range(0,len(Id)):
#             productId=Id
#             print(productId)


url="https://sale.jd.com/act/GrZjoT7UQWCn.html"
url2 = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv79456&productId="
url3="&score=0&sortType=5&pageSize=10&isShadowSku=0&page=0"
url4="&score=0&sortType=5&pageSize=10&isShadowSku=0&page="
productId =1993089
print(productId)
url0=url2+productId+url3
print("url0:",url0)
url1=url2+productId+url4
print("url1:",url1)



