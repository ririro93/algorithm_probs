from sys import stdin
from heapq import heappush, heappop

# stdin = open('input.txt', 'r')
input = stdin.readline 

# inputs
N = int(input())
X = [int(input()) for _ in range(N)]

# init
heap = []

# exe
for x in X:
    if x != 0:
        heappush(heap, -x)
    else:
        if heap:
            print(-heappop(heap))
        else:
            print(0)
            