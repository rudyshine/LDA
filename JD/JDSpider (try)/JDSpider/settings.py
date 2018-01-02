# -*- coding: utf-8 -*-

# Scrapy settings for JDSpider project
#
#
BOT_NAME = 'JDSpider'

SPIDER_MODULES = ['JDSpider.spiders']
NEWSPIDER_MODULE = 'JDSpider.spiders'

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
    # 'Y_type'
    # 'F_type',
    'X_type',
]