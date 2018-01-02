# -*- coding: utf-8 -*-

# Scrapy settings for JDSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'JDSpider'

SPIDER_MODULES = ['JDSpider.spiders']
NEWSPIDER_MODULE = 'JDSpider.spiders'



# FEED_URI = u'JDSpiderDoc_fan_L.csv'##电风扇
# FEED_URI = u'JDSpiderDoc_data_Y.csv'##源汁机
# FEED_URI = u'JDSpiderDoc_data_X.csv'##吸尘器 源汁机
# FEED_FORMAT = 'CSV'
#
# DOWNLOADER_MIDDLEWARES = {
#      'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':543,
#      'JDSpider.middlewares.MyproxiesSpiderMiddleware':125
# }
DOWNLOADER_MIDDLEWARES = {
#    'myproxies.middlewares.MyCustomDownloaderMiddleware': 543,
     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':None,
     'JDSpider.middlewares.MyproxiesSpiderMiddleware':125,
     'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware':None
}

FEED_EXPORTERS = {
    'csv': 'JDSpider.spiders.csv_item_exporter.MyProjectCsvItemExporter',
}
FIELDS_TO_EXPORT = [
    'p_Name',
    'shop_name',
    'ProductID',
    'price',
    'PreferentialPrice',
    'CommentCount',
    'GoodRateShow',
    'GoodCount',
    'GeneralCount',
    'PoorCount',
    'brand',
    'keyword',
    'type',
    'Y_type',
    'F_type',
    'X_type',
]