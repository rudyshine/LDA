import requests
from lxml.etree import HTML
import re

#url="http://list.gome.com.cn/cat10000198.html?intcmp=sy-1000053151-12"
url="http://item.gome.com.cn/A0006072601-pop8009372735.html"
rrr=requests.get(url).text
# print(rrr)
www=HTML(rrr)
# print(www)
#comment_web=www.xpath(".//div[@class='adv-main']")
comment_num=www.xpath(".//div[@class='prd-firstscreen-left']/div[@class='toolbar ']/span[@class='product-number']/text()")
#product_number_info=www.xpath(".//div[@class='adv-recommend']/div[@class='w-recommend']/span/text()")[0]
#p_Name=www.xpath(".//div[@class='item-tab-warp']/p[@class=item-name]/a/text()")
# shop_name=www.xpath(".//div[@class='item-tab-warp']/p[@class='item-shop']/span[@class='nnamezy']/text()")
# p_Name=www.xpath(".//div[@class='item-tab-warp']/p[@class='item-name']/a/text()")
# goods_info=www.xpath(".//div[@class='item-tab-warp']/p[@class='item-name']/a/@href")
# paper = www.xpath(".//li[@class='product-item']")[0]
print(comment_num)
# paper_start=paper.find('/')+1
# page=paper[paper_start:]
#
# #page = re.findall("/.*", paper) # 获取最大页数
# print (page)
#//*[@id="min-pager-number"]

'''''''''
comment_url="http://ss.gome.com.cn/item/v1/prdevajsonp/appraiseNew/9132986854/1/all/0/10/flag/appraise"
comment_web = requests.get(comment_url).text
bad_info = re.findall('"bad":\d+', comment_web)[0]
PoorCount = bad_info.split(':')[-1]  # 差评数
print(PoorCount)
good_info = re.findall('"good":\d+', comment_web)[0]
GoodCount = good_info.split(':')[-1]  # 好评数
print(GoodCount)
mid_info = re.findall('"mid":\d+', comment_web)[0]
GeneralCount = mid_info.split(':')[-1]  # 中评数
print(GeneralCount)
total_info = re.findall('"totalCount":\d+', comment_web)[0]
CommentCount = total_info.split(':')[-1]  # 评论总数
print(CommentCount)
# num=re.findall('"bad":\d+',ee)
# print(num)
'''''''''''
''''
price_url="http://ss.gome.com.cn/item/v1/d/m/store/unite/9132986854/1121870336/N/31180100/311801001/1/null/flag/item"
price_web = requests.get(price_url).text
price_info = re.findall('"salePrice":".*?"',price_web)[0]
price_1=price_info.split(':')[-1]
price_start=price_1.find('\"')+1
price_end=price_1.rfind('\"')
price=price_1[price_start:price_end]
preferentialPrice=price[:]
print(preferentialPrice)
'''''
'''''''''
[scrapy.core.scraper] ERROR: Spider error processing

"http://item.gome.com.cn/A0006072601-pop8009372735.html"
    product_number_info=info_1.xpath(".//span[@class='product-number']/text()").extract()[0]
IndexError: list index out of range

" http://item.gome.com.cn/A0005161241-pop8005428129.html"
    capacity_info=re.findall("容量：.*<",info_2.extract()[0])[-1]
IndexError: list index out of range

"http://review.gome.com.cn/A0006237240-0-1.html"
   comment_num=comment_web.xpath(".//div[@class='adv-tlayer']/span[@class='adv-prdcount']/strong/text()").extract()[0]
IndexError: list index out of range

" http://review.gome.com.cn/A0006328433-0-1.html"
    comment_num=comment_web.xpath(".//div[@class='adv-tlayer']/span[@class='adv-prdcount']/strong/text()").extract()[0]
IndexError: list index out of range

"http://item.gome.com.cn/A0005850539-pop8008829230.html"
    product_number_info=info_1.xpath(".//span[@class='product-number']/text()").extract()[0]
IndexError: list index out of range

,,"http://review.gome.com.cn/A0005589316-0-1.html"
    comment_num=comment_web.xpath(".//div[@class='adv-tlayer']/span[@class='adv-prdcount']/strong/text()").extract()[0]
IndexError: list index out of range

"http://review.gome.com.cn/A0006151513-0-1.html"
    comment_num=comment_web.xpath(".//div[@class='adv-tlayer']/span[@class='adv-prdcount']/strong/text()").extract()[0]
IndexError: list index out of range

"http://item.gome.com.cn/A0005754446-pop8008415049.html"
    product_number_info=info_1.xpath(".//span[@class='product-number']/text()").extract()[0]
IndexError: list index out of range



requests.exceptions.ConnectionError  HTTPConnectionPool
'''''''''''