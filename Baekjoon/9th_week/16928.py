from sys import stdin
from collections import deque

# stdin = open('input.txt', 'r')
input = stdin.readline

################################################ 뱀과 사다리 게임
# function
def BFS():
    # init
    deq = deque([1])
    Graph = [10000] * 100
    cnt = 1
    
    # exec
    while deq:
        num = len(deq)
        for _ in range(num):
            curr = deq.popleft()
            for n_node in dic[curr]:
                # 도착
                if n_node == 100:
                    return cnt

                # 도중
                if cnt < Graph[n_node]:
                    deq.append(n_node)
                    Graph[n_node] = cnt
        cnt += 1
    
################################################    
# inputs
N, M = map(int, input().split())
Jumps = [list(map(int, input().split())) for _ in range(N+M)]

# init
dic = {}
for i in range(1, 100):
    if i <= 94:
        dic[i] = list(range(i+1, i+7))
    else:
        dic[i] = list(range(i+1, 101))

for jump in Jumps:
    start = jump[1]
    if start <= 94:
        dic[jump[0]] = list(range(start+1, start+7))
    else:
        dic[jump[0]] = list(range(start+1, 101))

# exec
print(BFS())