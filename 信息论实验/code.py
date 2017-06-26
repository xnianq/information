#coding:utf-8
"""
author:xnianq
date : 2017/06/21
number : 2015211884
"""
import haffman,youcheng,suanshu
import optparse
import sys
if __name__ == '__main__':
    print\
"""
\33[1;36m|___ \ / _ \/ | ___|___ \/ / |( _ ) ( _ )| || |  
  __) | | | | |___ \ __) | | |/ _ \ / _ \| || |_ 
 / __/| |_| | |___) / __/| | | (_) | (_) |__   _|
|_____|\___/|_|____/_____|_|_|\___/ \___/   |_| 
author :xnianq,hfut,infosec 2015
"""

    parser = optparse.OptionParser(usage="python code.py -c %prog",prog=sys.argv[0])
    parser.add_option("-c","--code",action = "store",help ="haffman,youcheng,suanshu",type="string",dest = "codename")
    (options,args) = parser.parse_args()
    #print options
    if not  options.codename:
        print "usage 'python code.py -h' for help :)"
    try:
        code = options.codename
        if code == 'haffman':
            print "您当前选择的是\33[1;35mhuffman编码\33[1;36m\n"
            haffman.main()
        elif code == "youcheng":
            print "您当前选择的是\33[1;35m游程+huffman编码\33[1;36m\n"
            youcheng.youchengcode()
        elif code  == 'suanshu':
            print "您当前选择的是\33[1;35m算术编码\33[1;36m\n"
            suanshu.code()
    except  :
        print "请输入正确的编码名"