# 파이썬 내장 덱 사용

from collections import deque
from sys import stdin 

q = deque()

N = int(input(''))

for _ in range(N):
    command = stdin.readline().split()
    if command[0] == "push":
        q.append(command[1])
    elif command[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if q: print(q[0])
        else: print(-1)
        
    elif command[0] == "back":
        if q: print(q[len(q)-1])
        else: print(-1)
