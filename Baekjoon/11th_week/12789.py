from sys import stdin
from collections import deque

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())
A = deque(list(map(int, input().split())))

# init
i = 1
stack = []
sad = False

# exec
while A or stack:
    if A and A[0] == i:
        A.popleft()
        i += 1
    elif stack and stack[-1] == i:
        stack.pop()
        i += 1
    elif A:
        stack.append(A.popleft())
    else:
        sad = True
        print('Sad')
        break
    
if not sad:
    print('Nice')