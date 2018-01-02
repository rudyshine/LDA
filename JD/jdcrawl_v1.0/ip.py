# encoding=utf8
import codecs
from urllib import request
from bs4 import BeautifulSoup

# url = 'http://www.kuaidaili.com'
# html = request.urlopen(url).read()
# # print(html)
# # proxy = []
# soup = BeautifulSoup(html, "lxml")
# f = open("proxy.txt", "w")
# for link in soup.find_all("td",{"data-title":"IP"}):
#     ips = link.get_text()
#     print(type(ips))
#     f.write(ips)
#     f.write('\n')
# f.closed()


# # print(soup)
# f = open("proxy", "w")
# for link in soup.find_all("td"):
#     ips = link.get_text()
#     #     print(link)
#     print("ips:", ips)
#     f.write(ips)
#     f.write('\n')
# f.closed()
    # #


import urllib
import json
import socket
socket.setdefaulttimeout(10)
proxys = []
proxys.append({"http":"http://124.251.62.246:80"})
proxys.append({"http":"http://117.78.34.32:80"})
proxys.append({"http":"http://59.108.61.132:808"})
for id in range(0,5,1):
    try:
        url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv3104&productId=3889758&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0"
        res = urllib.urlopen(url,proxies=proxys[id%3]).read()
        res_json = json.loads(res)
        print(res_json['name'])
    except Exception as e:
        print(e)
        continue