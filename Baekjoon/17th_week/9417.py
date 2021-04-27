from sys import stdin
from math import gcd

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
M = int(input())
for _ in range(M):
    nums = list(map(int, input().split()))
    result =  - 2 ** 31
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            result = max(result, gcd(nums[i], nums[j]))
    print(result)
