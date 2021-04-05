from sys import stdin
from collections import deque

# stdin = open('input.txt', 'r')
input = stdin.readline

# functions
def DFS(start):
    deq = deque([start])

    while deq:
        l = len(deq)
        for _ in range(l):
            p = deq.popleft()
            for c in G[p]:
                if not checked[c]:
                    parents[c] = p
                    checked[c] = True
                    deq.append(c)

# inputs
N = int(input())
G = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

# init
parents = [0] * (N+1)
checked = [False] * (N+1)

# exec
checked[1] = True
DFS(1)
for parent in parents[2:]:
    print(parent)