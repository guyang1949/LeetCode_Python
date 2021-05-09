# -*- coding: utf-8 -*- 
# @Time : 2021/5/9 15:40 
# @Author : Alex Gu 
# @File : 20210509_0007_Reverse_Integer.py

def reverse(x: int) -> int:
    # result = 0
    # n = len(str(x))
    # print(n)
    # for i in range(n):
    #     temp = x // pow(10, i) % 10
    #     result = temp * pow(10, n - i - 1) + result
    # return result

    int_min, int_max = -2**31, 2**31 - 1
    result = 0
    while x != 0:
        if (result < (int_min // 10 + 1)) or (result > int_max // 10):
            return 0
        digit = x % 10
        # print(x,digit)
        if x < 0:
            if digit > 0:
                digit = digit - 10
        x = (x - digit) // 10
        result = result * 10 + digit
    return result

if __name__ == '__main__':
    x = int(input())

    print(reverse(x))

    print('program done')