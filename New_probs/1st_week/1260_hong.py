from sys import stdin, stdout
import sys
sys.setrecursionlimit(3000)
from collections import deque

def dfs(s):
    visited[s] = True
    dfs_result.append(s)
    for next_node in g[s]:
        if visited[next_node]:
            continue
        dfs(next_node)

def bfs(s):
    visited[s] = True
    bfs_result.append(s)
    queue = deque([s])
    while len(queue) > 0:
        l = len(queue)
        for _ in range(l):
            s = queue.popleft()
            for next_node in g[s]:
                if visited[next_node]:
                    continue
                visited[next_node] = True
                bfs_result.append(next_node)
                queue.append(next_node)

n, m, v = map(int, stdin.readline().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    g[a].append(b)
    g[b].append(a)

for i in range(1, n+1):
    g[i] = sorted(g[i])
    
print(g)

visited = [False for _ in range(n+1)]
dfs_result = []
dfs(v)
print(' '.join(map(str, dfs_result)))
bfs_result = []
visited = [False for _ in range(n+1)]
bfs(v)
print(' '.join(map(str, bfs_result)))