from sys import stdin
from collections import deque
from itertools import permutations

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())
A = list(input().split())
opers_cnt = list(map(int, input().split()))

# init
stack = []
for oper, cnt in zip(['+', '-', '*', '//'], opers_cnt):
    for _ in range(cnt):
        stack.append(oper)    
perms = set(list(permutations(stack)))
mn = 10 ** 9
mx = -10 ** 9

# exec
for perm in perms:
    result = ''
    for i in range(N-1):
        result +=  A[i]
        result += perm[i]
    result += A[N-1]
    val = eval(result)
    mn = min(mn, val)
    mx = max(mx, val)
print(mx)
print(mn)