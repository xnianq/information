#coding:utf-8

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
    def makecode(self,code):
        self._code = code
    def getcode(self):
        return self._code

def getnum(string):# 统计字符数量
    num = []
    dict = {}
    for i in range(0,26):
       num.append(float(string.count(chr(ord('a')+i)))/len(string))
    print "********************************************************************"
    print "字符频率统计为:"
    for i in range(0,26):
        if num[i]!=0:
            print "字符："+chr(ord('a')+i)+",频率为:"+str(num[i])
            dict[chr(ord('a')+i)]=num[i]
    print "********************************************************************"
    return dict
def getsortcharandnum(list):#进行排序
    return sorted(list.items(),key = lambda item:item[1])

def getfanotree(list,n):
    global nodelist
    nodelist = []
    num = 0;small = []
    for i in range(len(list)):
        nodelist.append(node(list[i][1],list[i][0]))
    root = node(1,'0')
    for i in range(len(nodelist)):
        num = num + nodelist[i].getdata()
        small.append(nodelist[i])
        if abs(num + nodelist[i + 1].getdata() - 1.0 / n) < abs(num + nodelist[i + 1].getdata() + nodelist[i + 2].getdata() - 1.0 / n):
            small.append(nodelist[i+1])
            num = num+nodelist[i+1].getdata()
            root.add(node(num,'0'))
            print num
            break
    #print num.getdata()
# def getfanocode(list,t,n):
#     num = 0
#     num2 = 0
#     small = []
#     big = []
#     t = float(t)
#     root = node()
#     if len(list)>n:
#         for i in range(len(list)):
#             num = num+list[i].getdata()
#             small.append(list[i])
#             if abs(num+list[i+1].getdata()-t/n)<abs(num+list[i+1].getdata()+list[i+2].getdata()-t/n):
#                 small.append(list[i+1])
#                 num = num+list[i+1].getdata()
#                 num2 = t-num
#                 num  = node(num,'0')
#                 num2 = node(num2,'0')
#                 print num.getdata(),num2.getdata()
#                 break
#     # else:
#     #
#     # if len(small) ==1:
#     #     num.add(small[0])
#     # if len(small)==n:
#     #     getfanocode(small,)
#
#     return num
if __name__ == '__main__':
    string = 'aaaaaaaaasssssssssssccccccccvvvvvvvvvggasdsadsadsa'
    list = getnum(string)
    list = getsortcharandnum(list)
    getfanotree(list,2)
