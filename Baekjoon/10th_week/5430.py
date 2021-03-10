from sys import stdin
from collections import deque

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
T = int(input())

# Test Cases
for _ in range(T):
    # inputs
    P = input().rstrip()
    N = int(input())
    X = input().rstrip()[1:-1]
    
    # init
    if N:
        X = deque(X.split(','))
    else:
        X = None
    left = True
    
    # exec
    if not X:
        if 'D' in P:
            print('error')
        else:
            print('[]')
    else:
        for p in P:
            if p == 'D':
                if X:
                    if left:
                        X.popleft()
                    else:
                        X.pop()
                else:
                    print('error')
                    break
            else:
                left = not left
        else:
            if left:
                print('[' + ','.join(list(X)) + ']')
            else:
                print('[' + ','.join(list(X)[::-1]) + ']')