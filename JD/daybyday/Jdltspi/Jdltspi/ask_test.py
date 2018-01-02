from bs4 import BeautifulSoup as bs
import re
import requests
from lxml.etree import HTML
url='https://www.jdbbs.com/thread-8318009-1-1.html'
r=requests.get(url).text
# print(r)
soup=bs(r,'lxml',from_encoding='utf-8')
div_id=re.compile(r'post_\d+')#定位每一条回复id
div=soup.find_all('div',id=div_id)
id_massage=re.compile(r'postmessage_\d+')#内容id
time_id=re.compile(r'authorposton\d+')#发表时间id
title='家用台式电暖器家电网友优惠59元包邮'
for i in range(len(div)):
    while i ==0:
        try:
            td=list(div[0].find('td',id=id_massage).stripped_strings)
            # print(td)
            # ask=td[6:]
            print(title)
            ask = td[6:]
            print('ask:')
            # print(ask)
        except:
            lock=div[i].find('div',class_='locked')
            em=lock.find('em')
            ask=em.text
            # print(ask)
        if len(ask)==0:
            ask_spe=div[i].select('div.pcbs h4 a')[0]
            print(ask_spe)
            ask=ask_spe.text
            print(ask)
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
    if i != 0:
        if div[i].find('div',class_='locked'):
            lock_else = div[i].find('div', class_='locked')
            em = lock_else.find('em')
            content = em.text
            print(content)
        elif not div[i].find('div',class_='locked'):
            try:
                td_else=list(div[i].find('td',id=id_massage).stripped_strings)
                # print(td_else)
                if '交易区新帖推荐' in td_else:
                    td_else.remove('交易区新帖推荐')
                try:
                    block = list(div[i].find('blockquote').stripped_strings)
                    # print(block)
                except:
                    # print('block找不到')
                    block=[]
                answer=[]
                for each in block:
                    if each in td_else:
                        td_else.remove(each)
                        if '发表于' not in each:
                            answer.append(each)
                for h in range(len(answer)):
                    answer[h]=re.sub(r'\xa0+',' ',answer[h])
                for h in range(len(td_else)):
                    td_else[h]=re.sub(r'\xa0+',' ',td_else[h])
                # print(block)
                # print(answer)
                print(td_else)
                try:
                    # 发表时间
                    em_authi = div[i].select('td.plc div.authi em')[0]
                    time_post = re.sub('发表于 ', '', em_authi.text)
                    print(time_post)
                    a_authi = div[i].select('td.pls div.authi a')[0]
                    # 发表作者
                    print(a_authi.text)
                except:
                    print('时间错误！')
            except:
                print("try 错误!")