from sys import stdin
from collections import deque

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())

# init
deq = deque()

# exec 
for _ in range(N):
    # input
    com = input().strip()
    
    # init
    if com[:4] == 'push':
        com, num = com.split()
    
    # exec
    if com == 'push':
        deq.append(num)
    elif com == 'pop':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif com == 'size':
        print(len(deq))
    elif com == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif com == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    else:
        if deq:
            print(deq[-1])
        else:
            print(-1)

