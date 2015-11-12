#coding:utf-8
__author__ = 'diaoshe'
"转换加密  每5个z一组拆分"
import re
def txtToPwd(txt):
    "加密"
    txt = txt.replace(' ','`') #替换空格
    s =(5 - len(txt)%5)%5
    while s>0:
        txt = txt + '^'
        s = s - 1

    grp = re.findall(r'.{5}',txt)

    finstr = ''
    for each in grp:

        finstr += each[::-1]# 字符串倒排
    print finstr
    return finstr



def pwdToTxt(pwd):
    grp = re.findall(r'.{5}',pwd)

    finstr = ''
    for each in grp:

        finstr += each[::-1]# 字符串倒排
    firstr = finstr.replace('`',' ').replace('^','')
    print firstr
    return finstr



if __name__ == "__main__":
    plain = raw_input("Please input your plain text: ")
    pwd = txtToPwd(plain)
    pwdToTxt(pwd)



