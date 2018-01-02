# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from JDSpider.settings import JD_user_agent
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import random



class JDUseragentMiddleware(UserAgentMiddleware):
    '''
    设置User-Agent
    '''
    def process_request(self, request, spider):
        agent=random.choice(JD_user_agent)
        if agent:
            request.headers.setdefault('User-Agent',agent)
