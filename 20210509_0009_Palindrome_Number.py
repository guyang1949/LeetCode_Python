# -*- coding: utf-8 -*- 
# @Time : 2021/5/9 16:41 
# @Author : Alex Gu 
# @File : 20210509_0009_Palindrome_Number.py

def isPalindrome_argorithm_1(x: int) -> bool:
    if x >= 0 or x < 2**32-1:
        n = len(str(x))
        reverse = 0
        for i in range(n):
            temp = x // pow(10, i) % 10
            reverse = temp * pow(10, n - i - 1) + reverse
        if reverse == x:
            return True
        else:
            return False
    else:
        return False

def isPalindrome_argorithm_2(x: int) -> bool:
    if x >= 0 or x < 2**32-1:
        x_str = str(x)
        n = len(x_str)
        l = len(x_str)//2
        # print(type(x_str))
        # print(n,l)
        j = 0
        for i in range(l):
            if x_str[i] == x_str[n-i-1]:
                j = j + 1
        if j == l:
            return True
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    x = int(input())

    print(isPalindrome_argorithm_1(x))

    print(isPalindrome_argorithm_2(x))

    print('program done')