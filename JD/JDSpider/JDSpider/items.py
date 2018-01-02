# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdspiderItem(scrapy.Item):

    #商品名称
    p_Name = scrapy.Field()
    #店铺名称
    shop_name = scrapy.Field()
    #商品ID
    ProductID = scrapy.Field()


    #正价
    price = scrapy.Field()
    #折扣价
    PreferentialPrice = scrapy.Field()



    # 评论总数
    CommentCount = scrapy.Field()
    # 好评度
    GoodRateShow = scrapy.Field()
    # 好评
    GoodCount = scrapy.Field()
    # 中评
    GeneralCount = scrapy.Field()
    # 差评
    PoorCount = scrapy.Field()
    #评论关键字
    keyword=scrapy.Field()

    #类别
    type=scrapy.Field()
    #控制方式
    # control_mode=scrapy.Field()
    #风扇叶数
    FBnumber=scrapy.Field()
    # #档位
    # gear=scrapy.Field()
    # #定时范围
    # Time_range=scrapy.Field()






