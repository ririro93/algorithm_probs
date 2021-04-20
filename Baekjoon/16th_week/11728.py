from sys import stdin
from collections import deque

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# init
result = []
a = b = 0

# exec
while a < N and b < M:
    if A[a] >= B[b]:
        result.append(B[b])
        b += 1
    else:
        result.append(A[a])
        a += 1
while a < N:
    result.append(A[a])
    a += 1
while b < M:
    result.append(B[b])
    b += 1
print(*result)
