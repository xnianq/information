# coding:utf-8

import copy
import math
global CODE
CODE = {}
class node:# 定义节点类，存储字符以及编码
    def __init__(self,data,char):
        self.data = data
        self.char = char
        self._children = []
    def getdata(self):
        return self.data
    def getchar(self):
        if self.char != '0':
            return self.char
        else :
            return False
    def getchildren(self):
        if len(self._children)==0:
            return False
        return self._children
    def add(self,node):
        self._children.append(node)
    def go(self,data):
        for child in self._children:
            if child.getdata() == data:
                return child
        return None
    def makecode(self,code):
        self._code = code
    def getcode(self):
        return self._code

def getnum(string):# 统计字符数量
    num = []
    gailv = []
    dict = {}
    for i in range(0,26):
       num.append(string.count(chr(ord('a')+i)))
    print "********************************************************************"
    print "字符个数统计为:"
    for i in range(0,26):
        if num[i]!=0:
            print "字符："+chr(ord('a')+i)+",个数为:"+str(num[i])
            dict[chr(ord('a')+i)]=num[i]
            gailv.append(float(num[i])/len(string))
    print "********************************************************************"

    return dict,gailv

def getsortcharandnum(list):#进行排序
    return sorted(list.items(),key = lambda item:item[1])



def getnewnode(i,n):# 生成新的节点，以及它的子孩子。
    #print nodelist[len(nodelist)-1].getdata()
    pop = []
    t = 0
    final = False
    for j in range(0,n):
        #print len(nodelist)
        #print nodelist[len(nodelist)-1].getdata(),nodelist[len(nodelist)-2].getdata()
        if  compare(nodelist[len(nodelist)-1].getdata(),nodelist[i+j].getdata()) :
            t = t + nodelist[i+j].getdata()
            pop.append(i+j)
        else:
            t = t+ nodelist[len(nodelist)-1].getdata()
            final =True
            nodefinal = nodelist[len(nodelist)-1]
            nodelist.pop(len(nodelist)-1)
    t = node(t, '0')
    if final:
        for i in range(0,n-1):
            t.add(nodelist[i])
        t.add(nodefinal)
    else:
        for i in range(0,n):
            t.add(nodelist[i])
    for i in range(len(pop)):
        nodelist.pop(0)
    nodelist.append(t)
    # print "nodelist"
    # for i in range(0,len(nodelist)):
    #     print nodelist[i].getdata()
    # print "\n"
    # print t.getdata()
    # print "t's children"
    # for i in range(len(t.getchildren())):
    #     print t.getchildren()[i].getdata()
    return t

def compare(num1,num2):#对两个数字进行比较
    if (num1-num2)>=0:
        return True
    else:
        return False

def buildhuffman(list,n):#将前N个数值进行相加，产生第一个节点。因为有补0的情况，所以不使用getnewnode方法
    for i in range(0,n):
        if (len(list)-n+i)%(n-1)==0:
            num0 = i
            break
    #print num0
    zero = []
    global nodelist
    nodelist =[]
    for i in range(len(list)):
        num = list[i][1]
        char  =list[i][0]
        nodelist.append(node(num,char))
    for i in range(0,num0):
        zero.append(node(num0,'0'))
    t = 0
    for i in range(0,n-num0):
        t = t+nodelist[i].getdata()
    t = node(t,'0')
    for i in range(0,num0):
        t.add(zero[i])
    for i in range(0,n-num0):
        t.add(nodelist[i])
    nodelist.append(t)
    for i in range(0,n-num0):
        nodelist.pop(0)
    if (float(len(list)-n)/(n-1)) == int((len(list)-n)/(n-1)):
        for i in range(0,(len(list)-n)/(n-1)):#在生成第一个节点之后使用getnewnode方法。
            getnewnode(0,n)
        # for i in range(0,len(nodelist)):
        #     print nodelist[i].getdata()
    else:
        for i in range(0, ((len(list) - n) / (n - 1))+1):  # 在生成第一个节点之后使用getnewnode方法。
            getnewnode(0, n)

    return nodelist #得到树。
def codehuffman(header,n):#对树进行编码，使用递归的思想。
    code = []
    for i in range(0,n):
        code.append(str(i))
    second = header.getchildren()
    if second!=False:
        for i in range(0,n):
            second[i].makecode(code[i])
            code1(second[i],n)
    huffmangetcode(header,n)
def code1(node1,n):
    global CODE
    if node1.getchildren():
        children = node1.getchildren()
        if children:
            for i in range(0,n):
                children[i].makecode(node1.getcode()+str(i))
                code1(children[i],n)

def huffmangetcode(header,n):# 对huffman编码进行输出。
    children = header.getchildren()
    if children!=False:
        for i in range(0,n):
            if children[i].getchar():
                CODE[children[i].getchar()]=children[i].getcode()
                print children[i].getchar()+":"+children[i].getcode()
            else:
                huffmangetcode(children[i],n)
def str2code(string):
    string2 = ""
    for i in range(len(string)):
        string2 = string2+CODE[string[i]]
    return string2
def getxiaolv(gailv,colen,chlen,n):
    hs = 0
    for i in range(len(gailv)):
        hs = hs+gailv[i]*math.log(1/gailv[i],2)
    #print hs
    t = float(colen)/chlen*math.log(float(n),2)
    xiaolv = hs/t
    return xiaolv
def code2str(code):
    string  = ""
    key_list = []
    value_list = []
    for key,value in CODE.items():
        key_list.append(key)
        value_list.append(value)
    t=0
    i=0
    while 1:
        if code[t:i] not in value_list:
            i = i+1
        else:
            get_value_index = value_list.index(code[t:i])
            string  = string + key_list[get_value_index]
            t = i
            i= i+1
        if t>=len(code):
            break
    return string
def main():
    test = raw_input("please input string you need code:")
    n = raw_input("请输入您需要编码的进制")
    list,gailv = getnum(test)
    list =  getsortcharandnum(list)
    #print list
    nodelist = buildhuffman(list,int(n))
    header = nodelist[0]
    print "字符编码为："
    codehuffman(header,int(n))
    print "********************************************************************"
    code =  str2code(test)
    print "编码为："
    print code
    print "解码为："
    print code2str(code)
    print "编码效率为："
    print getxiaolv(gailv,len(code),len(test),n)
if __name__ == '__main__':
    main()