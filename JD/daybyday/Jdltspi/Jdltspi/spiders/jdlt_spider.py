import pymongo
from Jdltspi.items import JdltspiItem
from bs4 import BeautifulSoup as bs
import re
from lxml.etree import HTML
import requests
import scrapy
from scrapy.selector import Selector
import time
class Jdltspider(scrapy.Spider):
    name = 'jdlt'
    allower_domain=['jdbbs.com']
    start_urls=[
    # 'https://wlliww.jdbbs.com/search.php?mod=forum&searchid=147&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=1',#格力
    #     'https://www.jdbbs.com/search.php?mod=forum&searchid=147&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=2',
    #             'https://www.jdbbs.com/search.php?mod=forum&searchid=1119&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=1', #美的
            # "https://www.jdbbs.com/search.php?mod=forum&searchid=1119&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=2"
        # 'https://www.jdbbs.com/search.php?mod=forum&searchid=404&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=1wo t' #大金1
    # 'https://www.jdbbs.com/search.php?mod=forum&searchid=404&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=2'
        'https://www.jdbbs.com/search.php?mod=forum&searchid=1651&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=1', ##洗碗机
        'https://www.jdbbs.com/search.php?mod=forum&searchid=1651&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=2'
    ]

    def parse(self, response):
        for each in response.xpath(".//div[@class='tl']/div[@id='threadlist']/ul/li/h3/a"):
            may_title=each.xpath(".//text()").extract()
            href_id=each.re('thread-(.*?)-1-1.html')[0]
            title=''
            for each in may_title:
                title=title[:]+each
            print(title)
            title = self.clean_data(title)
            item=JdltspiItem()
            href='https://www.jdbbs.com/thread-%s-1-1.html' % href_id
            # href='https://www.jdbbs.com/thread-8322581-1-1.html'
            #请求具体网页
            item=JdltspiItem()
            r=requests.get(url=href).text
            # time.sleep(10)
            try:
                num_max = int(re.findall('<span title="共 (\d+) 页', r)[0])
            except:
                num_max=None
            soup=bs(r,'lxml',from_encoding='utf-8')
            div_id=re.compile(r'post_\d+')
            div=soup.find_all('div',id=div_id)
            div_id = re.compile(r'post_\d+')  # 定位每一条回复id
            id_massage = re.compile(r'postmessage_\d+')  # 内容id
            ask=[]
            for i in range(len(div)):
                while i == 0:
                    try:
                        td = list(div[0].find('td', id=id_massage).stripped_strings)
                        # print(td)
                        if ('优惠'in title) or ('包邮' in title):
                            # print('消除')
                            ask=td[7:10]
                            for every in ask:
                                if '本帖' in every:
                                    ask.remove(every)
                            for a in range(len(ask)):
                                ask[a]=re.sub(r'\xa0+', ' ',ask[a])
                        else:
                            ask=td[6:]
                            for every in ask:
                                if '本帖' in every:
                                    ask.remove(every)
                        if len(ask) == 0:
                            ask_spe = div[i].select('div.pcbs h4 a')[0]
                            ask = ask_spe.text
                    except:
                        lock = div[i].find('div', class_='locked')
                        try:
                            em = lock.find('em')
                            ask.extend(em.text)
                        except:
                            pass
                    try:
                        # 发表时间
                        em_authi = div[0].select('td.plc div.authi em')[0]
                        time_post = re.sub('发表于 ', '', em_authi.text)
                        a_authi = div[0].select('td.pls div.authi a')[0]
                        user=a_authi.text
                    except:
                        print('时间作者失败！')
                    answer_first=None
                    content_first=None
                    ask=self.clean_data(ask)
                    item['href']=href
                    item['title']=title
                    item['ask'] = ask
                    item['time_now'] = time_post
                    item['user'] = user
                    item['answer'] = answer_first
                    item['content'] = content_first
                    yield item
                    break
                if i != 0:
                    answer=[]
                    if div[i].find('div', class_='locked'):
                        lock_else = div[i].find('div', class_='locked')
                        em = lock_else.find('em')
                        content = em.text
                        # print('这是内容：')
                        # print(content)
                    elif not div[i].find('div', class_='locked'):
                        try:
                            td_else = list(div[i].find('td', id=id_massage).stripped_strings)
                            # print(td_else)
                            if '交易区新帖推荐' in td_else:
                                td_else.remove('交易区新帖推荐')
                            try:
                                block = list(div[i].find('blockquote').stripped_strings)
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
                            # print(block)
                            # print(answer)
                            content=td_else
                            # print(td_else)
                            try:
                                # 发表时间
                                em_authi = div[i].select('td.plc div.authi em')[0]
                                time_post = re.sub('发表于 ', '', em_authi.text)
                                # print(time_post)
                                a_authi = div[i].select('td.pls div.authi a')[0]
                                # 发表作者
                                user=a_authi.text
                                # print(a_authi.text)
                            except:
                                print('时间错误！')
                        except:
                            print("try 错误!")
                        content=self.clean_data(content)
                        answer=self.clean_data(answer)
                        item['title']=None
                        item['ask']  =None
                        item['time_now']=time_post
                        item['user'] =user
                        item['answer'] =answer
                        item['content'] =content
                        item['href'] = None
                        yield item
            try:
                if num_max:
                    for x in range(2,num_max+1):
                        href_else = 'https://www.jdbbs.com/thread-%s-%d-1.html' % (href_id,x)
                        r_else=requests.get(href_else).text
                        time.sleep(10)
                        soup_else=bs(r_else,'lxml',from_encoding='utf-8')
                        div_else=soup_else.find_all('div', id=div_id)
                        for y in range(len(div_else)):
                            answer = []
                            if div_else[y].find('div', class_='locked'):
                                lock_else = div_else[y].find('div', class_='locked')
                                em = lock_else.find('em')
                                content = em.text
                                # print(content)
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
                                        answer=None
                                    # print(block)
                                    # print(answer)
                                    content = td_else
                                    # print(td_else)
                                    try:
                                        # 发表时间
                                        em_authi = div_else[y].select('td.plc div.authi em')[0]
                                        time_post = re.sub('发表于 ', '', em_authi.text)
                                        # print(time_post)
                                        a_authi = div_else[y].select('td.pls div.authi a')[0]
                                        # 发表作者
                                        user = a_authi.text
                                        # print(a_authi.text)
                                    except:
                                        print('时间错误！')
                                except:
                                    print("try 错误!")
                            answer=self.clean_data(answer)
                            content=self.clean_data(content)
                            item['title'] = None
                            item['ask'] =None
                            item['time_now'] = time_post
                            item['user'] = user
                            item['answer'] = answer
                            item['content'] = content
                            item['href'] = None
                            yield item

            except:
                pass

    def clean_data(self,cleandata):
        list=['董明珠','董大姐','董阿姨','董总','董小姐','董dj','董DJ','董*','董XX','董大妈','董贼','董事长']
        for each in list:
            if type(cleandata)==str:
                cleandata = re.sub(each,'', cleandata)
            else:
                for i in range(len(cleandata)):
                    cleandata[i]=re.sub(each,'',cleandata[i])
        return cleandata

