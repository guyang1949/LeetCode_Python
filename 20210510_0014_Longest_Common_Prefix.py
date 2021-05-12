# -*- coding: utf-8 -*- 
# @Time : 2021/5/10 9:32 
# @Author : Alex Gu 
# @File : 20210510_0014_Longest_Common_Prefix.py

def longestCommonPrefix_horizontal_scan(strs: list) -> str:
    if not strs:
        return ""

    lcp_str = strs[0]
    count = len(strs)

    def lcp(str1, str2):
        length = min(len(str1),len(str2))
        i = 0
        while i < length and str1[i] == str2[i]:
            i = i + 1
        return str1[:i]

    for i in range(count):
        lcp_str = lcp(lcp_str, strs[i])
        if not lcp_str:
            break
    return lcp_str

def longestCommonPrefix_vertical_scan(strs: list) -> str:
    if not strs:
        return ""

    length = len(strs[0])
    n = len(strs)

    for i in range(length):
        key = strs[0][i]
        for j in range(n):
            if i == len(strs[j]) or strs[j][i] != key:
                return strs[0][:i]
    return strs[0]

if __name__ == '__main__':
    temp = str(input())
    strs = [str(s) for s in temp.split()]

    result1 = longestCommonPrefix_horizontal_scan(strs)
    print(result1)

    result2 = longestCommonPrefix_vertical_scan(strs)
    print(result2)

    print('program done')