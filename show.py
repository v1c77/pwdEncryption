__author__ = 'Administrator'
# License：GPL v3 or higher.
# Copyright (C) 2012 Biergaizi

import sys

plain = input("Please input your plain text: ")
value = input("Please input your key(included negatives): ")

try:
    value = int(value)
except ValueError:
    print("Please input an integer.")
    sys.exit()

# a的ANSI码是97, z的ANSI码是122。
# A的ANSI码是65, Z的ANSI码是90。

print("")
print("secret: ", end='')

for letter in plain:
    # ansi_raw即没有经过任何处理的原始ANSI。
    ansi_raw = ord(letter)

    # ansi是经过移位加密的ANSI。
    ansi = ansi_raw + int(value)

    # 如果ansi_raw小于65或大于90，而且还不是小写字母，那么则说明它根本就不是字母。不加密，直接输出原始内容。
    if (ansi_raw < 65 or ansi_raw > 90) and letter.islower() == False:
        print(letter, end='')  # 如果ansi_raw小于97或大于122，而且还不是大写字母，那么则说明它根本不是字母。不加密，直接输出原始内容。
        elif (ansi_raw < 97 or ansi_raw > 122) and letter.isupper() == False:
        print(letter, end='')  # 否则，它就是字母。
        else:  # 如果它是大写字母，而且ANSI码大于90，则说明向后出界。那么通过这个公式回到开头，直到不出界为止。
        while letter.isupper() == True and ansi > 90:
            ansi = -26 + ansi

        # 如果它是大写字母，而且ANSI码小于65，则说明向前出界。那么通过这个公式回到结尾，直到不出界为止。
        while letter.isupper() == True and ansi < 65:
            ansi = 26 + ansi

        # 如果它是小写字母，而且ANSI码大于122，则说明向后出界。那么通过这个公式回到开头，直到不出界为止。
        while letter.isupper() == False and ansi > 122:
            ansi = -26 + ansi

        # 如果它是小写字母，而且ANSI码小于97，则说明向前出界。那么通过这个公式回到结尾，直到不出界为止。
        while letter.isupper() == False and ansi < 97:
            ansi = 26 + ansi

        # 将处理过的ANSI转换为字符，来输出密文。
        print(chr(ansi), end='')

    print("")
