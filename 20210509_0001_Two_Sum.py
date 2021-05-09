# -*- coding: utf-8 -*- 
# @Time : 2021/5/9 15:36 
# @Author : Alex Gu
# @File : 20210509_0001_Two_Sum.py

import time

def get_two_sum(nums: list, target: int) -> list:
    # print(nums)
    # print(target)
    print('normal algorithm')
    length = len(nums)
    tp = 0
    # print(length)
    for i in range(length):
        # print('mark')
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                print('%d + %d = %d' %(nums[i],nums[j],target))
                tp = 1
                # print([i,j])
                # return [i, j]
    if tp == 0:
        print('no match')
    return []

def get_two_sum_hash(nums: list, target: int) -> list:
    print('hash algorithm')
    hashtable = dict()
    tp = 0
    for i,num in enumerate(nums):
        # print(hashtable)
        if target - num in hashtable:
            print('%d + %d = %d' %(target-num,num,target))
            # print(nums[i])
            # print(i)
            return [hashtable[target-num],i]
            tp = 1
        hashtable[nums[i]] = i
        # print(hashtable,'',num)
    if tp == 0:
        print('no match')
    return []

if __name__ == '__main__':
    temp = input('')
    arr = [int(n) for n in temp.split()]
    num = int(input())

    start = time.time()
    get_two_sum(arr, num)
    end = time.time()
    print(str(end-start))

    start = time.time()
    get_two_sum_hash(arr,num)
    end = time.time()
    print(str(end - start))

    print('program done')