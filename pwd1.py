# coding:utf-8
__author__ = 'Administrator'

import sys

plain = raw_input("Please input your plain text: ")
value = input("Please input your key: ")

try:
    value = int (value)
except ValueError:
    print 'Please input an intger!'
    sys.exit()


# ASCI
# a-> 97    z->122
# A->65    Z->90

# print("")
# print("secret", end='')

for letter in plain:
    "ansi_row 是没有进过任何处理的absi字符"
    ansi_row = ord(letter)
    print 'ansi_row:'+str(ansi_row)


    "ansi是经过位移加密的ansi字符"


