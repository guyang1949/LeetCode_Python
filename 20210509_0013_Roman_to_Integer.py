# -*- coding: utf-8 -*- 
# @Time : 2021/5/9 19:42 
# @Author : Alex Gu 
# @File : 20210509_0013_Roman_to_Integer.py


def romanToInt(s: str) -> int:
    trans = dict()
    trans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # print(trans)
    l = len(s)
    result = 0
    # prenum = trans[s[0]]
    for i in range(l):
        if i == l-1:
            # print(result)
            if result >= trans[s[i]]:
                result = trans[s[i]] + result
            else:
                result = trans[s[i]] - result
            return result
        else:
            # print(i,l)
            if trans[s[i]] >= trans[s[i+1]]:
                result = trans[s[i]] + result
                # print(i,result,trans[s[i]],trans[s[i+1]])
            else:
                result = trans[s[i]] - result
                # print(i,result,trans[s[i]],trans[s[i+1]])

if __name__ == '__main__':
    s = str(input())

    print(romanToInt(s))

    print('program done')