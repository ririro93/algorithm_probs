from sys import stdin
from collections import deque

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
T = int(input())

# Test Cases
for _ in range(T):
    # inputs
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    
    # init
    sorted_P = sorted(P, reverse=True)
    deq = deque(list(range(N)))
    i = 0
    
    # exec   ->   지금 덱에서 최대값이 내 목표값보다 크면 실행
    while sorted_P[i] > P[M]:
        curr = deq.popleft()
        if P[curr] == sorted_P[i]:
            i += 1
            continue
        else:
            deq.append(curr)
    # 목표랑 같은 수 개수만큼 더하기
    for ele in deq:
        if ele == M:
            i += 1
            break
        if P[ele] == P[M]:
            i += 1
    print(i)
            