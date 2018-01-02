import requests
from bs4 import BeautifulSoup
import re

url='https://item.jd.com/11544794978.html'   #11544794978 729213  1653735732  3396573  14647052751  968231
r = requests.get(url, timeout=1000)
soup = BeautifulSoup(r.text, 'lxml')
print(soup)
# ips_capacity1 = soup.find_all('div', class_="Ptable-item")
# ips_capacity2 = soup.find_all('ul', class_="parameter2 p-parameter-list")
# ips_capacity = [ips_capacity1, ips_capacity2]
# for i in ips_capacity:
#     try:
#         capacity = re.findall(r'<dt>容量L</dt><dd>(.*?)<', str(ips_capacity))[0]
#     except IndexError:
#         try:
#             capacity = re.findall(r'li title=".*?">.*?容量：(.*?)<', str(ips_capacity))[0]
#         except IndexError:
#             capacity = 'none'
# print(capacity)

ips1 = soup.find_all('ul', class_="parameter2 p-parameter-list")
ips2 = soup.find_all('div', class_="detail-elevator-floor")
ips = [ips1, ips2]
for i in ips:
    brand = soup.find_all('ul', id="parameter-brand")
    brand = re.findall(r'<li title="(.*?)"', str(brand))[0]
    print(brand)
    # type = re.findall(r'<li title=".*?">.*?：(.*?)<', str(ips))
    # print(type)
    # X_name = re.findall(r'<li title=".*?">.*?商品名称：(.*?)<', str(ips))[0]
    # print(X_name)

##1973690539
# p_Name = each.xpath('div/div[@class="p-name"]/a/em/text()').extract()[0]