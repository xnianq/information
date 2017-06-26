#coding:utf-8
from math import log
gailv = [1.0/26,1.0/26,1.0/26,1.0/26,1.0/26,1.0/26,1.0/26,1.0/26,1.0/26,1.0/26,1.0/26,1.0/26,1.0/26,1.0/26,1.0/26,1.0/26,1.0/26,1.0/26,1.0/26,1.0/26,1.0/26,1.0/26,1.0/26,1.0/26,1.0/26,1.0/26]
Shuliang = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
num = 26
def encode(string):# 进行编码
    global num
    start = 0.0
    end = 1.0
    global strlen
    strlen = len(string)
    for i in range(len(string)):
        n =  ord(string[i])-ord('a')
        w = 0.0
        for k in range(n):
            w = w+gailv[k]
        lenth = end - start
        end = start + lenth*(w+gailv[n])
        start = start + lenth*w
        #print "start:"+str(start)+",end:"+str(end)
        Shuliang[n] = Shuliang[n]+1
        num = num+1
        for i in range(26):
            gailv[i] = float(Shuliang[i])/num
    result = start*0.01+end*0.99
    codelen = (-int(log(end-start,2)))+1
    print "the lenth you code is "+str(codelen)
    code = ""
    for i in range(codelen):
        code = code+str(int(result*2))
        result = result*2 - int(result*2)
    print "your code is "+code
    return  code
def decode(code):
    string = ""
    gailv = [1.0 / 26, 1.0 / 26, 1.0 / 26, 1.0 / 26, 1.0 / 26, 1.0 / 26, 1.0 / 26, 1.0 / 26, 1.0 / 26, 1.0 / 26,
             1.0 / 26, 1.0 / 26, 1.0 / 26, 1.0 / 26, 1.0 / 26, 1.0 / 26, 1.0 / 26, 1.0 / 26, 1.0 / 26, 1.0 / 26,
             1.0 / 26, 1.0 / 26, 1.0 / 26, 1.0 / 26, 1.0 / 26, 1.0 / 26]
    Shuliang = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    sum = 26
    result = 0.0
    t = 0.5
    for i in range(len(code)):
        result = result+int(code[i])*t
        t = t*0.5
    start = 0.0
    end= 1.0
    print num
    for i in range(strlen):
        lenth = end - start;t=0;wei = 0.0
        while (result-start)>wei*lenth:
            wei = wei+gailv[t]
            t = t+1
        t = t-1
        end = start + wei*lenth
        start = start+(wei-gailv[t])*lenth
        string = string + chr(t+ord('a'))
        Shuliang[t] = Shuliang[t]+1
        sum = sum +1
        for i in range(26):
            gailv[i] = float(Shuliang[i])/sum

    return string

def code():
    string = raw_input("请输入您要编码的字符串：")
    code = encode(string)
    string = decode(code)
    print string