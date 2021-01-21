from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())
start, goal = list(map(int, input().split()))
M = int(input())

G = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    G[x].append(y)
    G[y].append(x)
    
# function
def BFS(start):
    stack = [start]
    while stack:
        to = stack.pop()
        if to == goal:
            return visited[to]
        for g in G[to]:
            if visited[g] >= 0:
                continue
            visited[g] = visited[to] + 1 
            stack.append(g)
    return -1
            

# init
visited = [-1] * (N+1)
visited[start] = 0

# exe
print(BFS(start))
