import requests
from bs4 import BeautifulSoup
import re
import time

url='https://item.jd.com/10343440518.html'   #11544794978 729213  1653735732  3396573  14647052751  2640223
r = requests.get(url, timeout=1000)
soup = BeautifulSoup(r.text, 'lxml')
ips1 = soup.find_all('ul', class_="parameter2 p-parameter-list")
ips2 = soup.find_all('div', class_="detail-elevator-floor")
ips = [ips1, ips2]
# print(ips)
for i in ips:
    type = re.findall(r'<li title=".*?">.*?：(.*?)<', str(ips))
    X_name = re.findall(r'<li title=".*?">.*?商品名称：(.*?)<', str(ips))
    print(X_name)
#     try:
#         X_type = re.findall(r'<li title=".*?">类别：(.*?)<', str(ips))[0]
#     except IndexError:
#         try:
#             X_type = re.findall(r'<li title=".*?">类型：(.*?)<', str(ips))[0]
#         except IndexError:
#             X_type = re.findall(r'<li title=".*?">分类：(.*?)<', str(ips))[0]
# try:
#     shop_name = re.findall(r'<a clstag=".*?" href=".*?" target="_blank" title="(.*?)">', str(soup))[0]
# except IndexError:
#     shop_name = "none"
# try:
#     brand = soup.find_all('ul', id="parameter-brand")
#     brand = re.findall(r'<li title="(.*?)"', str(brand))[0]
# except IndexError:
#     brand = X_name
#     print(brand)