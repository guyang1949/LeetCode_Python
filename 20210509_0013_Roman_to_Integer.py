# -*- coding: utf-8 -*- 
# @Time : 2021/5/9 19:42 
# @Author : Alex Gu 
# @File : 20210509_0013_Roman_to_Integer.py


def romanToInt(s: str) -> int:
    trans = dict()
    trans = {'I': 1,
             'V': 5, 
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000
            }
    result = 0
    for i in range(len(s)-1):
        if trans[s[i]] < trans[s[i+1]]:
            result = result - trans[s[i]]
        else:
            result = result + trans[s[i]]
    result = result + trans[s[-1]]   # -1 is out of the dict rage so -1 stand for the last temp
    return result

if __name__ == '__main__':
    s = str(input())

    print(romanToInt(s))

    print('program done')