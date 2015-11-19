#coding:utf-8
__author__ = 'diaoshe'
"转换加密  每n个z一组拆分"
import re
def txtToPwd(txt,n=5):
    "加密"
    txt = txt.replace(' ','`') #替换空格
    s =(n - len(txt)%n)%n
    while s>0:
        txt = txt + '^'
        s = s - 1

    grp = re.findall(r'.{%s}' %n,txt)

    finstr = ''
    for i in range(0,n):
        for each in grp:

            finstr += each[i]# 字符串倒排
    print finstr
    return finstr



def pwdToTxt(pwd,n=5):
    p = pwd.__len__()/n
    grp = re.findall(r'.{%s}' %p,pwd)

    finstr = ''
    for i in range(0,p):

        for each in grp:

            finstr += each[i]
    firstr = finstr.replace('`',' ').replace('^','')
    print firstr
    return finstr



if __name__ == "__main__":
    plain = raw_input("Please input your plain text: ")
    n = int(raw_input("Plese input the key: "))
    pwd = txtToPwd(plain,n)
    pwdToTxt(pwd,n)



