from bs4 import BeautifulSoup
import requests
import random

def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[0].text + ':' + tds[1].text)
    return ip_list

def get_random_ip(ip_list,url1):
    # f = open("proxy.txt", "w")
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
        # f.write(proxy_list)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    html = requests.get(url2, headers=headers, timeout=10,proxies = proxies).text
    return html


if __name__ == '__main__':
    url = 'http://www.kuaidaili.com'
    url1="https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv3134&productId=3889758" \
         "&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0"
    url2="https://rate.tmall.com/list_detail_rate.htm?itemId=543801975609&spuId=569641085" \
         "&sellerId=3079263591&order=3&currentPage=1&append=0&content=1&tagId=&posi=&" \
         "picture=&ua=059UW5TcyMNYQwiAiwQRHhBfEF8QXtHcklnMWc%3D%7CUm5Ockt%2FQXxJdE5xRX9Bfyk" \
         "%3D%7CU2xMHDJ7G2AHYg8hAS8XLQMjDUsqTDBBbzlv%7CVGhXd1llXGhWa15jWWZSaFZoX2JAeER%2BQ3" \
         "xDfkR%2FRXxHeUF0TmA2%7CVWldfS0QMAg9AyMfKgokWzJJZQZ1GytRIkcmdhMsCCNqRBJE%7CVmhIGCcS" \
         "Mg8vEy4TJwc5DTcKKhYrFC0NNww5GSUYJx4%2BBDkCVAI%3D%7CV25OHjAePgQ4DS0TLxMzCzUPO207%7CWGF" \
         "BET9UM1UoRSNecFBoXWNDfEZ9XWdZZlwKXA%3D%3D%7CWWBAED4QMAsyByceIB8%2FCjEPNWM1%7CWmFBET" \
         "9aIgwsEC8RMQwsGCEfI3Uj%7CW2JCEjwSMgo%2FCysVIB8%2FAz8HPABWAA%3D%3D%7CXGVFFTsVNQw5DS0" \
         "RLRUoCDQKMQUxZzE%3D%7CXWVFFTsVNWVcZlNzT3NKfykJNBQ6FDQINgI3CV8J%7CXmdaZ0d6WmVFeUB8XG" \
         "JaYEB5WWVYeExsWXlGfFxnR39fY10L&isg=As3NGEzYqVJhKQ1cB-gs5t6F3OA7UwF8SGl9Ow9S3mTBBuy41v" \
         "vPTNnUBiyb&needFold=0&_ksTS=1493080744558_2197&callback=jsonp2198"
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    # }
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
    }
    ip_list = get_ip_list(url, headers=headers)
    proxies = get_random_ip(ip_list,url1)
    print("proxies:",proxies)