from sys import stdin
from collections import deque

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
T = int(input())

# Test Cases
for _ in range(T):
    # inputs
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    
    # init
    if D < 0:
        D = 360 + D
    turns = int(D // 45)
    changed_into = [x-turns if x-turns >= 0 else x-turns+8 for x in range(8)]
    # print(turns)
    # print(changed_into)
    
    deqs = [deque() for _ in range(8)]
    
    for r in range(N):
        for c in range(N):
            if r == c and r < N//2:
               deqs[0].append(X[r][c])
            elif c == N//2 and r < N//2:
                deqs[1].append(X[r][c])
            elif r+c == N-1 and r < c:
                deqs[2].append(X[r][c])
            elif r == N//2 and c > N//2:
                deqs[3].appendleft(X[r][c])
            elif r == c and r > N//2:
                deqs[4].appendleft(X[r][c])
            elif c == N//2 and r > N//2:
                deqs[5].appendleft(X[r][c])
            elif r+c == N-1 and r > c:
                deqs[6].appendleft(X[r][c])
            elif r == N//2 and c < N//2:
                deqs[7].append(X[r][c]) 
    # for deq in deqs:
    #     print(deq)
        
    # exec
    for r in range(N):
        for c in range(N):
            if r == c and r < N//2:
               X[r][c] = deqs[changed_into[0]].popleft()
            elif c == N//2 and r < N//2:
               X[r][c] = deqs[changed_into[1]].popleft()
            elif r+c == N-1 and r < c:
               X[r][c] = deqs[changed_into[2]].popleft()
            elif r == N//2 and c > N//2:
               X[r][c] = deqs[changed_into[3]].pop()
            elif r == c and r > N//2:
               X[r][c] = deqs[changed_into[4]].pop()
            elif c == N//2 and r > N//2:
               X[r][c] = deqs[changed_into[5]].pop()
            elif r+c == N-1 and r > c:
               X[r][c] = deqs[changed_into[6]].pop()
            elif r == N//2 and c < N//2:
               X[r][c] = deqs[changed_into[7]].popleft()
    
    for row in X:
        print(*row)
    