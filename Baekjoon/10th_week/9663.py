from sys import stdin
from collections import deque

# stdin = open('input.txt', 'r')
input = stdin.readline

# functions
def back(N, K):
    # init
    global cnt
    i = K
    
    # exec
    if N == K:
        cnt += 1
        return
    for j in range(N):
        if checked_col[j] or checked_diag1[i+j] or checked_diag2[i-j+N-1]:
            continue
        checked_col[j] = True
        checked_diag1[i+j] = True
        checked_diag2[i-j+N-1] = True
        back(N, K+1)
        checked_col[j] = False
        checked_diag1[i+j] = False
        checked_diag2[i-j+N-1] = False
        
# inputs
N = int(input())

# init
checked_col = [False] * N
checked_diag1 = [False] * (2*N - 1)
checked_diag2 = [False] * (2*N - 1)

cnt = 0

# exec
back(N, 0)
print(cnt)
        