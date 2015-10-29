# coding:utf-8
from __future__ import print_function
import sys
__author__ = 'Administrator'


plain = raw_input("Please input your plain text: ")
value = input("Please input your key: ")

try:
    value = int (value)
except ValueError:
    print('Please input an intger!')
    sys.exit()
# ------------上面为加密法1

# ASCI
# a-> 97    z->122
# A->65    Z->90


print("secret:",end='')

for letter in plain:
    "ansi_row 是没有进过任何处理的absi字符"
    ansi_row = ord(letter)
    # print 'ansi_row:'+str(ansi_row)

    # ansi 是经过位移后加密的ANSI
    ansi_sec = ansi_row + int(value)
    # print 'ansi_new:' + str(ansi_sec),
    # 如果ansi_raw<65 或>90且还不是小写字母，那么说明他不是字母//->直接输出原内容
    if (ansi_row < 65 or ansi_row > 90) and letter.islower() == False:
        print(letter,end='')
        #如果小于97大于122 还不是大写字母，说明根本不是字母，不加密直接输出
    elif (ansi_row < 97 or ansi_row > 122) and letter.isupper() == False:
        print(letter,end='')
    #剩下的都是字母,如果是大写字母 且加密后ansi>90说明想或出界，此方法回到开头知道符合为止
    else:
        while letter.isupper() == True and ansi_sec > 90:
            ansi_sec = -26 + ansi_sec

        #如果是大写字母 但是 密文ansi码小于65说明向前出界，那么通过此公式回到结尾，知道不出界为止
        while letter.isupper() == True and ansi_sec < 65:
            ansi_sec = 26 + ansi_sec

        #同理如果原文为小写字母 但是密文ansi码大于122 ，说明向后出界， 通过循环令其归位
        while letter.islower() == True and ansi_sec > 122:
            ansi_sec = -26 + ansi_sec

        #如果原文小写，密文ansi码 小于97 说明向前出界，循环归位
        while letter.islower() ==True and ansi_sec <97:
            ansi_sec = 26 + ansi_sec

    print(chr(ansi_sec),end='')




    "ansi是经过位移加密的ansi字符"


