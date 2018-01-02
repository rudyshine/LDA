# import requests
# import json
# import re
#
# json_url_keyword = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv79456&score=0&sortType=5&pageSize=10&isShadowSku=0&page=0&productId=1993070'
# r = requests.get(json_url_keyword)
# html = r.content.decode('gb2312', 'ignore')
# keywords = re.findall(r',"name":(.*?),', html)
# for i in range(len(keywords)):
#     keywords[i] = str(keywords[i])
# keyword = ''
# keyword = keyword.join(keywords)
# print(keyword)

import requests
import json
import re
#
# json_url_keyword = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv79456&score=0&sortType=5&pageSize=10&isShadowSku=0&page=0&productId=1993070'
# r = requests.get(json_url_keyword)
# html = r.content.decode('gb2312', 'ignore')
# keywords = re.findall(r',"name":"(.*?)",', html)
# keyword=' '.join(keywords)
# # mth=re.findall('"(.*?)"',keyword)
# # for m in mth:
# #     print(m)
# # keyword=re.sub(r" "" ","",keyword)
# print(keyword)
# #
#!/usr/bin/python
# import json
# import requests
#
# url='https://club.jd.com/comment/productPageComments.action?' \
#     'callback=fetchJSON_comment98vv79456&productId=1993070&score=0&sortType=5' \
#     '&pageSize=10&isShadowSku=0&page=0'
#
# jsonData = 'fetchJSON_comment98vv79456({"productAttr":null,"productCommentSummary":{"goodRateShow":98,"poorRateShow":1,"poorCountStr":"700+","averageScore":5,"generalCountStr":"500+","showCount":10000,"showCountStr":"1万+","goodCount":48000,"generalRate":0.01,"generalCount":500,"skuId":1993070,"goodCountStr":"4.8万+","poorRate":0.014,"afterCount":600,"goodRateStyle":146,"poorCount":700,"skuIds":null,"poorRateStyle":2,"generalRateStyle":2,"commentCountStr":"4.9万+","commentCount":49000,"productId":1993070,"afterCountStr":"600+","goodRate":0.976,"generalRateShow":1},"hotCommentTagStatistics":[{"id":1072191,"name":"服务很好","status":0,"rid":3152,"productId":1993070,"count":2939,"created":"2015-11-09 16:04:14","modified":"2017-06-21 10:50:10","type":0,"canBeFiltered":false},{"id":1075935,"name":"送货快","status":0,"rid":3163,"productId":1993070,"count":2739,"created":"2015-11-12 01:25:10","modified":"2017-06-21 10:50:10","type":0,"canBeFiltered":false},{"id":1075936,"name":"安装速度","status":0,"rid":3164,"productId":1993070,"count":2576,"created":"2015-11-12 01:25:10","modified":"2017-06-21 10:50:10","type":0,"canBeFiltered":false},{"id":1077616,"name":"空调质量好","status":0,"rid":3159,"productId":1993070,"count":1934,"created":"2015-11-12 23:51:20","modified":"2017-06-21 10:16:46","type":0,"canBeFiltered":false},{"id":1076418,"name":"机器漂亮","status":0,"rid":3157,"productId":1993070,"count":1592,"created":"2015-11-12 12:43:25","modified":"2017-06-21 10:10:20","type":0,"canBeFiltered":false},{"id":1078818,"name":"制冷效果好","status":0,"rid":3151,"productId":1993070,"count":1445,"created":"2015-11-13 17:57:44","modified":"2017-06-21 08:15:25","type":0,"canBeFiltered":false},{"id":1071761,"name":"声音小","status":0,"rid":3154,"productId":1993070,"count":1302,"created":"2015-11-09 11:37:22","modified":"2017-06-21 09:29:50","type":0,"canBeFiltered":false},{"id":1080147,"name":"制冷速度快","status":0,"rid":3153,"productId":1993070,"count":1206,"created":"2015-11-14 20:55:31","modified":"2017-06-21 10:16:46","type":0,"canBeFiltered":false},{"id":1076325,"name":"制冷比较快","status":0,"rid":3162,"productId":1993070,"count":1096,"created":"2015-11-12 11:43:33","modified":"2017-06-21 10:16:46","type":0,"canBeFiltered":false},{"id":1075934,"name":"外机噪音小","status":0,"rid":3155,"productId":1993070,"count":1005,"created":"2015-11-12 01:25:10","modified":"2017-06-21 09:09:40","type":0,"canBeFiltered":false}],"jwotestProduct":"99","maxPage":100,"score":0,"soType":5,"imageListCount":500,"vTagStatistics":[],"comments":[{"id":10494415492,"guid":"8b959f6a-f97c-4383-9b79-d7c71fcc8255","content":"必须好评，安装配送都是一流服务，太专业了买空调必须格力，怕双十一抢不着提前预订提前使用，活动力度都很大一次买俩。。安装师傅搞完还顺带收拾走了垃圾。点个赞，谁都不喝。","creationTime":"2017-06-10 14:15:05","isTop":true,"referenceId":"1993070","referenceImage":"jfs/t4225/144/2186856210/49250/9dcb6b30/58cd009eN8e0b0eb3.jpg","referenceName":"格力（GREE）大1匹 定速 品圆 冷暖 壁挂式空调 KFR-26GW/(26592)NhDa-3","referenceTime":"2017-06-01 10:22:25","referenceType":"Product","referenceTypeId":0,"firstCategory":737,"secondCategory":794,"thirdCategory":870,"replies":[],"replyCount":14,"score":5,"status":1,"title":"","usefulVoteCount":12,"uselessVoteCount":0,"userImage":"storage.360buyimg.com/i.imageUpload/6a645f3634363864383837393763623131343937303830393433383036_sma.jpg","userImageUrl":"storage.360buyimg.com/i.imageUpload/6a645f3634363864383837393763623131343937303830393433383036_sma.jpg","userLevelId":"105","userProvince":"","viewCount":0,"orderId":0,"isReplyGrade":false,"nickname":"木***铖","userClient":0,"images":[{"id":344153517,"associateId":218395206,"productId":0,"imgUrl":"//img30.360buyimg.com/n0/s128x96_jfs/t6055/321/2121622632/47589/e2489e1b/593b8e36N2c324444.jpg","available":1,"pin":"","dealt":0,"imgTitle":"","isMain":0},{"id":344153518,"associateId":218395206,"productId":0,"imgUrl":"//img30.360buyimg.com/n0/s128x96_jfs/t6637/129/213792132/38213/d5936610/593b8e3aN2b190d0f.jpg","available":1,"pin":"","dealt":0,"imgTitle":"","isMain":0},{"id":344153519,"associateId":218395206,"productId":0,"imgUrl":"//img30.360buyimg.com/n0/s128x96_jfs/t5671/4/3369444237/39370/2df8da7e/593b8e40N78062d92.jpg","available":1,"pin":"","dealt":0,"imgTitle":"","isMain":0},{"id":344153520,"associateId":218395206,"productId":0,"imgUrl":"//img30.360buyimg.com/n0/s128x96_jfs/t6565/344/208290600/42170/6cb85044/593b8e45Nc47f5ee4.jpg","available":1,"pin":"","dealt":0,"imgTitle":"","isMain":0}],"showOrderComment":{"id":218395206,"guid":"c72e415d-7fa4-462e-97cf-34b3247b37c5","content":"必须好评，安装配送都是一流服务，太专业了买空调必须格力，怕双十一抢不着提前预订提前使用，活动力度都很大一次买俩。。安装师傅搞完还顺带收拾走了垃圾。点个赞，谁都不喝。';
#
# text = json.loads(jsonData)
# text=text['CommentsCount'][0]
# GoodCount=text['GoodCountStr']
# print('GoodCount:',GoodCount)
# print(json.loads('CommentsCount'))

# import json
# import requests
#
# jsonData = 'fetchJSON_comment98vv79456({"productAttr":null,"productCommentSummary":{"goodRateShow":98,"poorRateShow":1,"poorCountStr":"700+","averageScore":5,"generalCountStr":"500+","showCount":10000,"showCountStr":"1万+","goodCount":48000,"generalRate":0.01,"generalCount":500,"skuId":1993070,"goodCountStr":"4.8万+","poorRate":0.014,"afterCount":600,"goodRateStyle":146,"poorCount":700,"skuIds":null,"poorRateStyle":2,"generalRateStyle":2,"commentCountStr":"4.9万+","commentCount":49000,"productId":1993070,"afterCountStr":"600+","goodRate":0.976,"generalRateShow":1},"hotCommentTagStatistics":[{"id":1072191,"name":"服务很好","status":0,"rid":3152,"productId":1993070,"count":2939,"created":"2015-11-09 16:04:14","modified":"2017-06-21 10:50:10","type":0,"canBeFiltered":false},{"id":1075935,"name":"送货快","status":0,"rid":3163,"productId":1993070,"count":2739,"created":"2015-11-12 01:25:10","modified":"2017-06-21 10:50:10","type":0,"canBeFiltered":false},{"id":1075936,"name":"安装速度","status":0,"rid":3164,"productId":1993070,"count":2576,"created":"2015-11-12 01:25:10","modified":"2017-06-21 10:50:10","type":0,"canBeFiltered":false},{"id":1077616,"name":"空调质量好","status":0,"rid":3159,"productId":1993070,"count":1934,"created":"2015-11-12 23:51:20","modified":"2017-06-21 10:16:46","type":0,"canBeFiltered":false},{"id":1076418,"name":"机器漂亮","status":0,"rid":3157,"productId":1993070,"count":1592,"created":"2015-11-12 12:43:25","modified":"2017-06-21 10:10:20","type":0,"canBeFiltered":false},{"id":1078818,"name":"制冷效果好","status":0,"rid":3151,"productId":1993070,"count":1445,"created":"2015-11-13 17:57:44","modified":"2017-06-21 08:15:25","type":0,"canBeFiltered":false},{"id":1071761,"name":"声音小","status":0,"rid":3154,"productId":1993070,"count":1302,"created":"2015-11-09 11:37:22","modified":"2017-06-21 09:29:50","type":0,"canBeFiltered":false},{"id":1080147,"name":"制冷速度快","status":0,"rid":3153,"productId":1993070,"count":1206,"created":"2015-11-14 20:55:31","modified":"2017-06-21 10:16:46","type":0,"canBeFiltered":false},{"id":1076325,"name":"制冷比较快","status":0,"rid":3162,"productId":1993070,"count":1096,"created":"2015-11-12 11:43:33","modified":"2017-06-21 10:16:46","type":0,"canBeFiltered":false},{"id":1075934,"name":"外机噪音小","status":0,"rid":3155,"productId":1993070,"count":1005,"created":"2015-11-12 01:25:10","modified":"2017-06-21 09:09:40","type":0,"canBeFiltered":false}],"jwotestProduct":"99","maxPage":100,"score":0,"soType":5,"imageListCount":500,"vTagStatistics":[],"comments":[{"id":10494415492,"guid":"8b959f6a-f97c-4383-9b79-d7c71fcc8255","content":"必须好评，安装配送都是一流服务，太专业了买空调必须格力，怕双十一抢不着提前预订提前使用，活动力度都很大一次买俩。。安装师傅搞完还顺带收拾走了垃圾。点个赞，谁都不喝。","creationTime":"2017-06-10 14:15:05","isTop":true,"referenceId":"1993070","referenceImage":"jfs/t4225/144/2186856210/49250/9dcb6b30/58cd009eN8e0b0eb3.jpg","referenceName":"格力（GREE）大1匹 定速 品圆 冷暖 壁挂式空调 KFR-26GW/(26592)NhDa-3","referenceTime":"2017-06-01 10:22:25","referenceType":"Product","referenceTypeId":0,"firstCategory":737,"secondCategory":794,"thirdCategory":870,"replies":[],"replyCount":14,"score":5,"status":1,"title":"","usefulVoteCount":12,"uselessVoteCount":0,"userImage":"storage.360buyimg.com/i.imageUpload/6a645f3634363864383837393763623131343937303830393433383036_sma.jpg","userImageUrl":"storage.360buyimg.com/i.imageUpload/6a645f3634363864383837393763623131343937303830393433383036_sma.jpg","userLevelId":"105","userProvince":"","viewCount":0,"orderId":0,"isReplyGrade":false,"nickname":"木***铖","userClient":0,"images":[{"id":344153517,"associateId":218395206,"productId":0,"imgUrl":"//img30.360buyimg.com/n0/s128x96_jfs/t6055/321/2121622632/47589/e2489e1b/593b8e36N2c324444.jpg","available":1,"pin":"","dealt":0,"imgTitle":"","isMain":0},{"id":344153518,"associateId":218395206,"productId":0,"imgUrl":"//img30.360buyimg.com/n0/s128x96_jfs/t6637/129/213792132/38213/d5936610/593b8e3aN2b190d0f.jpg","available":1,"pin":"","dealt":0,"imgTitle":"","isMain":0},{"id":344153519,"associateId":218395206,"productId":0,"imgUrl":"//img30.360buyimg.com/n0/s128x96_jfs/t5671/4/3369444237/39370/2df8da7e/593b8e40N78062d92.jpg","available":1,"pin":"","dealt":0,"imgTitle":"","isMain":0},{"id":344153520,"associateId":218395206,"productId":0,"imgUrl":"//img30.360buyimg.com/n0/s128x96_jfs/t6565/344/208290600/42170/6cb85044/593b8e45Nc47f5ee4.jpg","available":1,"pin":"","dealt":0,"imgTitle":"","isMain":0}],"showOrderComment":{"id":218395206,"guid":"c72e415d-7fa4-462e-97cf-34b3247b37c5","content":"必须好评，安装配送都是一流服务，太专业了买空调必须格力，怕双十一抢不着提前预订提前使用，活动力度都很大一次买俩。。安装师傅搞完还顺带收拾走了垃圾。点个赞，谁都不喝。';
#
# text = json.loads(jsonData)
# print('text:',text)
#


# import scrapy
# url="https://search.jd.com/Search?keyword=%E5%8E%9F%E6%B1%81%E6%9C%BA&enc=utf-8&pvid=c899e53965754020863ddbcbb4414b72"
# import codecs
# from bs4 import BeautifulSoup
# url="https://item.jd.com/"+ str(1959718783)+".html"
# r = requests.get(url)
#
# soup = BeautifulSoup(r.text, 'lxml')
# print("soup:",soup)
# ips = soup.find_all('ul',class_="parameter2 p-parameter-list")
# print(ips)
# 类别 = re.findall(r'<li title=".*?">类别：(.*?)<', str(ips))[0]
# print(类别)
# 控制方式=re.findall(r'<li title=".*?">控制方式：(.*?)<', str(ips))
# print(控制方式[0])
# 扇叶片数=re.findall(r'<li title=".*?">扇叶片数：(.*?)<', str(ips))
# print(扇叶片数[0])
# 档位=re.findall(r'<li title=".*?">档位：(.*?)<', str(ips))
# print(档位[0])
# 定时范围=re.findall(r'<li title=".*?">定时范围：(.*?)<', str(ips))
# print(定时范围[0])
#
# from bs4 import BeautifulSoup
# product_typ_url = "https://item.jd.com/" + 1959718783 + ".html"
# r = requests.get(product_typ_url)
# soup = BeautifulSoup(r.text, 'lxml')
# ips = soup.find_all('ul', class_="parameter2 p-parameter-list")
# type = re.findall(r'<li title=".*?">类别：(.*?)<', str(ips))[0]
# control_mode = re.findall(r'<li title=".*?">控制方式：(.*?)<', str(ips))[0]
# FBnumber = re.findall(r'<li title=".*?">扇叶片数：(.*?)<', str(ips))[0]
# gear = re.findall(r'<li title=".*?">档位：(.*?)<', str(ips))[0]
# Time_range = re.findall(r'<li title=".*?">定时范围：(.*?)<', str(ips))[0]

# from bs4 import BeautifulSoup
# url="https://item.jd.com/"+ str(12947900725)+".html" ##1959718783  1069555  2640223  1419129  2770990
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
# ips1=soup.find_all('ul', class_="parameter2 p-parameter-list")
# ips2=soup.find_all('div', class_="detail-elevator-floor")
# ips = [ips1, ips2]
# print(ips)
# # try:
# for i in ips:
#     type = re.findall(r'<li title=".*?">(.*?)：(.*?)<', str(ips))
#     type_data=[]
#     for j in type :
#         head = j[1].split(' ')[0]  # 提取键值
#         found = False
#         idx = 0
#         for r in type_data:  # 看键值是否存在
#             if r[0] == head:
#                 found = True;
#                 break
#             idx = idx + 1
#         if found:
#             type_data[idx][1].append(j)  # 存在直接追加
#         else:
#             type_data.append([head, [j]])  # 不存在创建新list
#             # Tuple化
# list3 = []
# for e in type_data:
#     list3.append((e[0], tuple(e[1])))
# list3 = tuple(list3)
# print(list3)
        # print(type[j])
        # control_mode = re.findall(r'<li title=".*?">控制方式：(.*?)<', str(ips))[0]
        # FBnumber = re.findall(r'<li title=".*?">扇叶片数：(.*?)<', str(ips))[0]
        # break
# except IndexError:
#     type="没有对应数据"
#     print(type)
# except NameError:
#     control_mode="没有对应数据"
#     print(control_mode)



# print(type)
# print(control_mode)
# print(control_mode)

from bs4 import BeautifulSoup

product_typ_url = "https://item.jd.com/2770990.html"
r = requests.get(product_typ_url, timeout=1000)
soup = BeautifulSoup(r.text, 'lxml')
shop_name = re.findall(r'<a clstag=".*?" href=".*?" target="_blank" title="(.*?)">', str(soup))[0]
try:
    brand = soup.find_all('ul', id="parameter-brand")
    brand = re.findall(r'<li title="(.*?)"', str(brand))[0]
except IndexError:
    brand = "None"
ips1 = soup.find_all('ul', class_="parameter2 p-parameter-list")
ips2= soup.find_all('div', class_="detail-elevator-floor")
ips = [ips1, ips2]
for i in ips:
        type_data = re.findall(r'<li title=".*?">.*?：(.*?)<', str(ips))
        try:
            type = re.findall(r'<li title=".*?">.*?吸头：(.*?)<', str(ips))[0]
        except IndexError:
            type="none"
        try:
            type_f = re.findall(r'<li title=".*?">类别：(.*?)<', str(ips))[0]
        except IndexError:
            type_f="none"
        try:
            type_y = re.findall(r'<li title=".*?">类型：(.*?)<', str(ips))[0]
        except IndexError:
            type_y="none"
print("type_data",type_data)
print("type",type)
print("type_f",type_f)
print("type_y",type_y)