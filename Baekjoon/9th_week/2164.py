from sys import stdin
from collections import deque

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())

# init
i = 0
deq = deque(list(range(1, N+1)))

# exec
while len(deq) > 1:
    if i % 2 == 0:
        deq.popleft()
        pass
    else:
        item = deq.popleft()
        deq.append(item)
        pass
    i += 1
    
print(deq[-1])