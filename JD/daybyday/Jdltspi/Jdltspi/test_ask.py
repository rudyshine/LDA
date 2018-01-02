import requests
import time
import re
from bs4 import BeautifulSoup as bs
import csv
title='等会买松下UE13KK1怡涵去！格力的东西以后都不看，售后态度很差'
href_id='8362078'
href='https://www.jdbbs.com/thread-%s-1-1.html' % href_id
with open('test_jdlt.csv','w',newline='',encoding='utf-8') as fin:
    writer=csv.writer(fin)
    writer.writerow(['title','ask','time_now','user','answer','content'])
    #请求具体网页
    r=requests.get(url=href).text
    # time.sleep(10)
    # r_max=requests.get(url=href).text
    try:
        num_max = int(re.findall('<span title="共 (\d+) 页', r)[0])
    except:
        num_max=None
        print('这个帖子只有一页')
    # html=HTML(r)
    soup=bs(r,'lxml',from_encoding='utf-8')
    div_id=re.compile(r'post_\d+')
    div=soup.find_all('div',id=div_id)
    div_id = re.compile(r'post_\d+')  # 定位每一条回复id
    # div = soup.find_all('div', id=div_id)
    id_massage = re.compile(r'postmessage_\d+')  # 内容id
    # time_id = re.compile(r'authorposton\d+')  # 发表时间id
    ask=[]
    try:
        if num_max:
            for x in range(2,num_max+1):
                href_else = 'https://www.jdbbs.com/thread-%s-%d-1.html' % (href_id,x)
                print(href_else)
                r_else=requests.get(href_else).text
                time.sleep(10)
                soup_else=bs(r_else,'lxml',from_encoding='utf-8')
                div_else=soup_else.find_all('div', id=div_id)
                for y in range(len(div_else)):
                    answer = []
                    # content=[]
                    if div_else[y].find('div', class_='locked'):
                        lock_else = div_else[y].find('div', class_='locked')
                        em = lock_else.find('em')
                        content = em.text
                        print(content)
                    elif not div_else[y].find('div', class_='locked'):
                        try:
                            td_else = list(div_else[y].find('td', id=id_massage).stripped_strings)
                            # print(td_else)
                            if '交易区新帖推荐' in td_else:
                                td_else.remove('交易区新帖推荐')
                            try:
                                block = list(div_else[y].find('blockquote').stripped_strings)
                                # print(block)
                            except:
                                # print('block找不到')
                                block = []

                            for each in block:
                                if each in td_else:
                                    td_else.remove(each)
                                    if '发表于' not in each:
                                        answer.append(each)
                            for h in range(len(answer)):
                                answer[h] = re.sub(r'\xa0+', ' ', answer[h])
                            for h in range(len(td_else)):
                                td_else[h] = re.sub(r'\xa0+', ' ', td_else[h])
                            if len(answer) == 0:
                                answer = None
                            # print(block)
                            # print(answer)
                            content = td_else
                            print(td_else)
                            try:
                                # 发表时间
                                em_authi = div_else[y].select('td.plc div.authi em')[0]
                                time_post = re.sub('发表于 ', '', em_authi.text)
                                print(time_post)
                                a_authi = div_else[y].select('td.pls div.authi a')[0]
                                # 发表作者
                                user = a_authi.text
                                print(a_authi.text)
                            except:
                                print('时间错误！')
                        except:
                            print("try 错误!")
                        item = {
                            'title': title,
                            'ask': ask,
                            'time_now': time_post,
                            'user': user,
                            'answer': answer,
                            'content': content
                        }
                        print(item)
                        writer.writerow([title, ask, time_post, user, answer, content])
    except:
        pass
