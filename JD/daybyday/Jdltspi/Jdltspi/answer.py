from bs4 import BeautifulSoup as bs
import re
import requests
from lxml.etree import HTML
url='https://www.jdbbs.com/thread-8355987-1-1.html'
r=requests.get(url).text
# print(r)
soup=bs(r,'lxml',from_encoding='utf-8')
div_id=re.compile(r'post_\d+')
div=soup.find_all('div',id=div_id)
id_massage=re.compile(r'postmessage_\d+')
time_id=re.compile(r'authorposton\d+')#发表时间id
# for i in range(len(div)):
#     try:
#         if i ==0:
#             a_authi=div[i].select('td.pls div.authi a')[0]
#             print(a_authi.text)
#     except:
#         print('Wrong!')
#         pass
# num_max=int(re.findall('<span title="共 (\d+) 页',r)[0])
# print(num_max)
title='格力】家用台式电暖器家电网友优惠59元包邮'
for i in range(len(div)):
    while i ==0:
        try:
            td=list(div[0].find('td',id=id_massage).stripped_strings)
            # print(td)
            if '优惠券' or '包邮' in title:
                ask=td[7:10]
            else:
                ask = td[6:]
            print(ask)
        except:
            lock=div[i].find('div',class_='locked')
            em=lock.find('em')
            ask=em.text
            # print(ask)
        try:
            # 发表时间
            em_authi=div[0].select('td.plc div.authi em')[0]
            time_post=re.sub('发表于 ','',em_authi.text)
            print(time_post)
            a_authi = div[0].select('td.pls div.authi a')[0]
            # 发表作者
            print(a_authi.text)
        except:
            print('时间作者失败！')
        break