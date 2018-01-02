# import web
# import sys
#
# urls = ("/Service/hello", "hello")
# app = web.application(urls, globals())
#
#
# class hello:
#     def GET(self):
#         return 'Hello,world!';
#
#
# if __name__ == "__main__":
#     app.run()
# import pymongo
# lient = pymongo.MongoClient("localhost",27017)
# print(lient)

"https://rate.tmall.com/list_detail_rate.htm?itemId=543802723409&spuId=702887145&sellerId=3079263591&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&ua=069UW5TcyMNYQwiAiwQRHhBfEF8QXtHcklnMWc%3D%7CUm5Ockt%2FQ3ZCdktxTHdIfSs%3D%7CU2xMHDJ7G2AHYg8hAS8XLQMjDUsqTDBBbzlv%7CVGhXd1llXGhUYVVhXGZbYF9qXWBCeE1yTHNHe0N2T3dCeE13WQ8%3D%7CVWldfS0RMQ05AzkZJR8%2FETYRNEYnSW0TfR8vHzsGd0kkClwK%7CVmhIGCcSMg8vEy4TJwc5DTcKKhYrFC0NNww5GSUYJx4%2BBDkCVAI%3D%7CV2xMHDJXLwEhHSIcPAEhHSgSLXst%7CWGFBET8RMQk2CSkVKBwpCTINMwheCA%3D%3D%7CWWFBET8RMWFYZFp6RnpDelpkUWpIcFBvWmRGek91TW1RblFxTXQiAj8fMR8%2FBD8KP2k%2F%7CWmNeY0N%2BXmFBfUR4WGZeZER9XWNefkpqVmw6&isg=ApSUQ-7qsKs4xCRXpo-Ffc86Zdvth7jXOaZUcC51a5-yGTVjVvwVZmLbb6d6&needFold=0&_ksTS=1491899077570_1747&callback=jsonp1748"
# import random
# ran_num = random.sample(range(0, 6900), 6900)
# s = set(ran_num)
# print("s is: ",s)
# r1 = random.sample(range(0, 6900), 2)
# print("r1 is:",r1)
# s1 = set(r1)
# print("s1 is :",s1)
# r2 = s - s1
# print("r2 is :",r2)
# s2=list(r2)
# # print("s2 is :",s2)
# for i in range(34):
#     if i == 2:
#         continue
#     print(i)
import random

n=2
# b=getmaxpage
if int(7)>=n:
    m=int(7)//n
    ran_num = range(int(7))
    for i in range(m):
        s = set(ran_num)
        ran1=random.sample(ran_num, n)
        print("ran1 is :", ran1)
        s1 = set(ran1)
        print("s1 is :",s1)

        s2 = s - s1
        ran_num=list(s2)

    ran_num=random.sample(ran_num)
    print(ran_num)



        # print("ran_num[i+1] is :", ran)
        # ran_num=random.sample(range(0, int(sumpage)), int(sumpage))
        # s=set(ran_num)
        # r1=random.sample(ran_num,n)
        # print("r1 is :", r1)
        # s1=set(r1)
        # s2=s-s1
        # r2=ran_num
        # print("r2 is :", r2)
        # r3=random.sample(r2,n)
        # print("r3 is :",r3)
        #
        # print("set:",s)
        # r1 =random.sample(range(0, int(sumpage)), n)
        # set1=set(r1)
        # set2=set-set1
        # print("set2:",set2)
        # return 0