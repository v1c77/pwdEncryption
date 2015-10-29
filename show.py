__author__ = 'Administrator'
# License��GPL v3 or higher.
# Copyright (C) 2012 Biergaizi

import sys

plain = input("Please input your plain text: ")
value = input("Please input your key(included negatives): ")

try:
    value = int(value)
except ValueError:
    print("Please input an integer.")
    sys.exit()

# a��ANSI����97, z��ANSI����122��
# A��ANSI����65, Z��ANSI����90��

print("")
print("secret: ", end='')

for letter in plain:
    # ansi_raw��û�о����κδ����ԭʼANSI��
    ansi_raw = ord(letter)

    # ansi�Ǿ�����λ���ܵ�ANSI��
    ansi = ansi_raw + int(value)

    # ���ansi_rawС��65�����90�����һ�����Сд��ĸ����ô��˵���������Ͳ�����ĸ�������ܣ�ֱ�����ԭʼ���ݡ�
    if (ansi_raw < 65 or ansi_raw > 90) and letter.islower() == False:
        print(letter, end='')  # ���ansi_rawС��97�����122�����һ����Ǵ�д��ĸ����ô��˵��������������ĸ�������ܣ�ֱ�����ԭʼ���ݡ�
        elif (ansi_raw < 97 or ansi_raw > 122) and letter.isupper() == False:
        print(letter, end='')  # ������������ĸ��
        else:  # ������Ǵ�д��ĸ������ANSI�����90����˵�������硣��ôͨ�������ʽ�ص���ͷ��ֱ��������Ϊֹ��
        while letter.isupper() == True and ansi > 90:
            ansi = -26 + ansi

        # ������Ǵ�д��ĸ������ANSI��С��65����˵����ǰ���硣��ôͨ�������ʽ�ص���β��ֱ��������Ϊֹ��
        while letter.isupper() == True and ansi < 65:
            ansi = 26 + ansi

        # �������Сд��ĸ������ANSI�����122����˵�������硣��ôͨ�������ʽ�ص���ͷ��ֱ��������Ϊֹ��
        while letter.isupper() == False and ansi > 122:
            ansi = -26 + ansi

        # �������Сд��ĸ������ANSI��С��97����˵����ǰ���硣��ôͨ�������ʽ�ص���β��ֱ��������Ϊֹ��
        while letter.isupper() == False and ansi < 97:
            ansi = 26 + ansi

        # ���������ANSIת��Ϊ�ַ�����������ġ�
        print(chr(ansi), end='')

    print("")
