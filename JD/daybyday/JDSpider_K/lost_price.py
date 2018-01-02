import requests
import time
import codecs
import pandas as pd

def get_price(ProductID):
    json_url_p='http://p.3.cn/prices/mgets?skuIds=J_' + ProductID
    try:
        data = requests.get(json_url_p, timeout=1000).json()[0]
        price = data['m']
        PreferentialPrice = data['p']
    except requests.exceptions.ConnectionError:  # requests.exceptions.ReadTimeout
        print('Timeout ConnectionError1:json_url_p')
        time.sleep(600)
        try:
            data = requests.get(json_url_p, timeout=1000).json()[0]
            price = data['m']
            PreferentialPrice = data['p']
        except requests.exceptions.ConnectionError:
            print('Timeout ConnectionError2:json_url_p')
            time.sleep(3600)
            data = requests.get(json_url_p, timeout=1000).json()[0]
            price = data['m']
            PreferentialPrice = data['p']
        except requests.exceptions.ReadTimeout:
            print('Timeout,ReadTimeout:', json_url_p)
    except requests.exceptions.ReadTimeout:
        print('Timeout,ReadTimeout:', json_url_p)
    data = pd.DataFrame({'ProductID': [ProductID],'price':[price],'PreferentialPrice': [PreferentialPrice]})
    table = data.set_index('price')
    table.head()
    data.to_csv('prince_data.csv',mode='a',header=False)
    print("done save csv....")

if __name__ == '__main__':
    inforead = codecs.open("inforead.txt", 'r', 'utf-8')
    print('Read file:')
    ProductID = inforead.readline()
    while ProductID!="":
        ProductID = ProductID.rstrip('\r\n')
        get_price(ProductID)
        ProductID = inforead.readline()