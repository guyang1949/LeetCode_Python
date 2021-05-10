# -*- coding: utf-8 -*- 
# @Time : 2021/5/10 9:32 
# @Author : Alex Gu 
# @File : 20210510_0014_Longest_Common_Prefix.py

def longestCommonPrefix_horizontal_scan(strs: list) -> str:
    if not strs:
        return ""

    lcp_str = strs[0]
    count = len(strs)

    for i in range(count):
        print(i,lcp_str,strs[i])
        lcp_str = lcp(lcp_str, strs[i])
        if not lcp_str:
            break
    return lcp_str

def lcp(str1, str2):
    length = min(len(str1),len(str2))
    i = 0
    while i < length and str1[i] == str2[i]:
        i = i + 1
    return str1[:i]

if __name__ == '__main__':
    temp = str(input())
    strs = [str(s) for s in temp.split()]

    # print(strs)
    result = longestCommonPrefix_horizontal_scan(strs)
    print(result)

    print('program done')