# -*- coding: utf-8 -*-
# 手动设置ip

# import random
# from scrapy import signals
# from JDSpider.settings import IPPOOL
#
#
# class MyproxiesSpiderMiddleware(object):
#     def __init__(self, ip=''):
#         self.ip = ip
#
#     def process_request(self, request, spider):
#         thisip = random.choice(IPPOOL)
#         print("this is ip:" + thisip["ipaddr"])
#         request.meta["proxy"] = "http://" + thisip["ipaddr"]

import random
import time

class MyproxiesSpiderMiddleware(object):
    """docstring for ProxyMiddleWare"""

    def process_request(self, request, spider):
        '''对request对象加上proxy'''
        proxy = self.get_random_proxy()
        print("this is request ip:" + proxy)
        request.meta['proxy'] = proxy

    def process_response(self, request, response, spider):
        '''对返回的response处理'''
        # 如果返回的response状态不是200，重新生成当前request对象
        if response.status != 200:
            proxy = self.get_random_proxy()
            print("this is response ip:" + proxy)
            # 对当前reque加上代理
            request.meta['proxy'] = proxy
            return request
        return response

    def get_random_proxy(self):
        '''随机从文件中读取proxy'''
        while 1:
            with open('proxies.txt', 'r') as f:
                proxies = f.readlines()
            if proxies:
                break
            else:
                time.sleep(1)
        proxy = random.choice(proxies).strip()
        return proxy
