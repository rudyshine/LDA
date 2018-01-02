# #去掉空格及特殊字符串
# s='   hello,word!'
# print(s.strip())
# print(s)
# print(s.lstrip('  hello,'))
# print(s.rstrip('!'))
#
# ##连接字符串
# s1='abd'
# s2='ccc'
# s1+=s2
# print(s1)
# print(s2)
#
#
# ##查找字符串(<0表示没有找到)
# s1='strchr'
# s2='r'
# nPos=s1.index(s2)
# print(nPos)
#
# ##比较字符
# import operator
# s1='strchrsxsa'
# s2='strch'
# print(operator.gt(s1,s2))      #意思是greater than（大于）
# print(operator.ge(s1,s2))     #意思是greater and equal（大于等于）
# print(operator.eq(s1,s2))    #意思是equal（等于）
# print(operator.le(s1,s2))   #意思是less and equal（小于等于）
# print(operator.lt(s1,s2))    #意思是less than（小于）
#
# ##字符串大小写
# s1="ASDzxc"
# s1=s1.upper() #大写
# print(s1)
# s1=s1.lower()##小写
# print(s1)

# ##翻转字符串
# s1='abcdefg'
# s1=s1[::-1]
# print(s1)

# ##查找字符串(完全匹配)
# s1='abcdefg'
# s2='g'
# print(s1.find(s2))


##分割字符串
s1='ab,cde,fgh,ijk'
print(s1)
print(s1.split(','))


#计算字符串中出现频率次数最多的字母
import string

def get_max_value(text):
    text=text.lower()
    return max(string.ascii_lowercase,key=text.count)

if __name__ == '__main__':
    text='fadsfdfdfd#￥%《》gfdgfdgAASSWCDFV'
    get_max_value(text)

    print(max(string.ascii_lowercase,key=text.count))


##正则表达式

