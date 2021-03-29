from sys import stdin
from collections import deque
# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
S = list(input().rstrip())
T = list(input().rstrip())

# init
deq = deque(T)
flipped = False

# exec
while True:
    if flipped:
        curr = deq[0]
    else:
        curr = deq[-1]

    if curr == 'A':
        if flipped:
            deq.popleft()
        else:
            deq.pop()
    else:
        if flipped:
            deq.popleft()
        else:
            deq.pop()
        flipped = not flipped
    # print(deq, flipped)
    if len(deq) == len(S):
        if not flipped and list(deq) == S:
            print(1)
        elif flipped and list(deq) == S[::-1]:
            print(1)
        else:
            print(0)
        break