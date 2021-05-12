# -*- coding: utf-8 -*- 
# @Time : 2021/5/12 17:05 
# @Author : Alex Gu 
# @File : 20210512_0020_Valid_Parentheses.py

def isVaild(s: str) -> bool:
    dic = {'{': '}',
           '[': ']',
           '(': ')',
           '!': '!'}
    stack = ['!']
    for c in s:
        if c in dic:
            stack.append(c)
        elif dic[stack.pop()] != c:
            return False
    return len(stack) == 1 # if len(stack) == 1 return ture

if __name__ == '__main__':

    s = str(input())

    result = isVaild(s)
    print(result)

    print('program done')