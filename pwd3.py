#coding:utf-8
__author__ = 'diaoshe'
import sys

"多字母替换加密"
"""
    获取info and key
    层叠求余
    key 可复用


"""
chartonum = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
chartonum_upper ={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
numtochar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numtochar_upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def txtTopwd(plain, key):
    "加密"
    key_len = len(key)
    pwd = ''
    i = 1 # 设置计数器
    for each in plain:
        n = i%key_len - 1 #获取对应的ｋ中字母
        if each.isalpha:
            "只操作字符"
            if each.islower():
                "如果字符为小写"
                if key[n].islower():
                    "如果key小写则使用小写字典"
                    add = chartonum[each] + chartonum[key[n]]
                    pwd_num = add%26
                    pwd = pwd + numtochar[pwd_num]
                elif key[n].isupper():
                    "key大写"
                    add = chartonum[each] + chartonum_upper[key[n]]
                    pwd_num = add%26

                    pwd = pwd + numtochar[pwd_num]


            elif each.isupper():
                "如果信息字符为大写"
                if key[n].islower():
                    "如果key小写则使用小写字典"
                    add = chartonum_upper[each] + chartonum[key[n]]
                    pwd_num = add%26

                    pwd = pwd + numtochar_upper[pwd_num]

                elif key[n].isupper():
                    "key大写"
                    add = chartonum_upper[each] + chartonum_upper[key[n]]
                    pwd_num = add%26

                    pwd = pwd + numtochar_upper[pwd_num]

            else:
                pwd = pwd + each
        i = i + 1

    print pwd
    return pwd

def pwdToTxt(pwd,key):

    "解密"
    key_len = len(key)
    new_value = ''
    i = 1 # 设置计数器
    for each in pwd:
        n = i%key_len - 1 #获取对应的ｋ中字母
        if each.isalpha:
            "只操作字符"
            if each.islower():
                "如果字符为小写"
                if key[n].islower():
                    "如果key小写则使用小写字典"

                    add = chartonum[each] - chartonum[key[n]]
                    new_value_num = add%26
                    new_value = new_value + numtochar[new_value_num]
                elif key[n].isupper():
                    "key大写"
                    add = chartonum[each] - chartonum_upper[key[n]]

                    # add = chartonum[each] + chartonum_upper[key[n]]
                    new_value_num = add%26

                    new_value = new_value + numtochar[new_value_num]


            elif each.isupper():
                "如果信息字符为大写"
                if key[n].islower():
                    "如果key小写则使用小写字典"
                    add = chartonum_upper[each] - chartonum[key[n]]

                    # add = chartonum_upper[each] + chartonum[key[n]]
                    new_value_num = add%26

                    new_value = new_value + numtochar_upper[new_value_num]

                elif key[n].isupper():
                    "key大写"
                    add = chartonum_upper[each] - chartonum_upper[key[n]]

                    # add = chartonum_upper[each] + chartonum_upper[key[n]]
                    new_value_num = add%26

                    new_value = new_value + numtochar_upper[new_value_num]

            else:
                new_value = new_value + each
        i = i + 1

    print new_value
    return new_value




if __name__ == "__main__":
    "主函数"
    plain = raw_input("Please input your plain text: ")
    key = raw_input("Please input your key:")
    # plain = 'information'
    # key = 'STAR'
    print "plain:" + plain
    print "key:" + key

    pwd = txtTopwd(plain, key)
    new_valude = pwdToTxt(pwd,key)
