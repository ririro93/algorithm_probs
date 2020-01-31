from collections import deque
from sys import stdin

deq = deque()

N = int(input(''))

for _ in range(N):
    command = stdin.readline().split()
    if command[0] == 'push_front':
        deq.append(command[1])
    elif command[0] == 'push_back':
        deq.appendleft(command[1])
    elif command[0] == 'pop_front':
        if deq: print(deq.pop())
        else: print(-1)
    elif command[0] == 'pop_back':
        if deq: print(deq.popleft())
        else: print(-1)
    elif command[0] == 'size':
        print(len(deq))
    elif command[0] == 'empty':
        if deq: print(0)
        else: print(1)
    elif command[0] == 'front':
        if deq: print(deq[len(deq) - 1])
        else: print(-1)
    elif command[0] == 'back':
        if deq: print(deq[0])
        else: print(-1)
    else:
        print('wrong command')
