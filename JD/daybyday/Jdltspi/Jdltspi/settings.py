# -*- coding: utf-8 -*-

# Scrapy settings for Jdltspi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Jdltspi'

SPIDER_MODULES = ['Jdltspi.spiders']
NEWSPIDER_MODULE = 'Jdltspi.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Jdltspi (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 15
AUTOTHROTTLE_ENABLED = True
FIELDS_TO_EXPORT = [
    'title',
    'ask',
    'answer',
    'content',
    'time_now',
    'user',
    'href'

]
ITEM_PIPELINES = {
   # 'sunings.pipelines.SuningsPipeline': 300,
    'Jdltspi.pipelines.CSVPipeline':200
}

LOG_FILE='LOG.txt'