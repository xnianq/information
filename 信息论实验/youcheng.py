# coding:utf-8

import haffman


def gethuffman(test,n):
    list,gailv = haffman.getnum(test)
    list = haffman.getsortcharandnum(list)
# print list
    nodelist = haffman.buildhuffman(list, int(n))
    header = nodelist[0]
    print "huffman字符编码为："
    haffman.codehuffman(header, int(n))
    code =  haffman.str2code(test)
    print "********************************************************************"
    return code

def getyoucheng(string):
    cod = ""
    i = 0
    count = 1
    char = []
    num = []
    while 1:
        if string[i]==string[i+1]:
            i = i+1
            count = count +1
        else:
            #print count
            num.append(count)
            char.append(string[i])
            i = i+1
            count = 1
        if i == len(string)-1:
            char.append(string[i])
            num.append(count)
            break
    maxlen = max(num)
   # print maxlen
   # print bin(max)
    maxlen =  len(bin(maxlen)[2:])
    # for i in range(len(num)):
    #     print bin(num[i])[2:].zfill(maxlen)
    print "游程编码长度为"+str(maxlen)
    for i in range(len(char)):
        cod = cod+ haffman.CODE[char[i]]+bin(num[i])[2:].zfill(maxlen)
    print "您最后得到的编码为："+cod
    return  cod,maxlen
def encode(string):
    gethuffman(string,2)
    cod,lenth = getyoucheng(string)
    return cod,lenth
def decode(code,lenth):
    i = 0
    t = 0
    string  = ""
    key_list = []
    value_list = []
    for key,value in haffman.CODE.items():
        key_list.append(key)
        value_list.append(value)
    while 1:
        if code[t:i] not in value_list:
            i = i+1
        else:
            get_value_index = value_list.index(code[t:i])
            string  = string + key_list[get_value_index]*eval("0b"+code[i:i+lenth])
            t = i+lenth
            #print eval(code[i:i+lenth])
            #print t
            i= i+1
        if t>=len(code):
            break
    print "译码为："+string
    return string

def youchengcode():
    string = raw_input("请输入您要编码的内容：")
    coe,lenth = encode(string)
    decode(coe,lenth)



#youchengcode()
