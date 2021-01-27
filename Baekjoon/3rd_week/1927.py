# from sys import stdin

# stdin = open('input.txt', 'r')
# input = stdin.readline

'''
# 1. deque 사용 -> 시간초과 뜬다(당연히 sorted 때문에ㅎㅎ..)
from collections import deque

## inputs
N = int(input())
cmds = []
for _ in range(N):
    cmds.append(int(input()))

## init
deq = deque()
mx = 0
mn = 2 ** 31

## exe
for cmd in cmds:
    if cmd == 0:
        if deq:
            print(deq.popleft())
        else:
            print(0)
    else:
        if cmd <= mn:
            deq.appendleft(cmd)
        elif mx <= cmd:
            deq.append(cmd)
        else:
            deq.append(cmd)
            deq = deque(sorted(deq))
        mx = max(mx, cmd)
        mn = min(mn, cmd)
'''      
        
# 2. 힙 사용
import heapq, sys
input = sys.stdin.readline

## inputs
N = int(input())
cmds = []
for _ in range(N):
    cmds.append(int(input()))
    
## init
heap = []

## exe
for cmd in cmds:
    if cmd == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, cmd)



