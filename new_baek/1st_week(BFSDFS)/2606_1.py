import sys
def dfs(matrix, start):
    for i in matrix[start]:
        if i not in visited:
            visited.add(i)
            dfs(matrix, i)           

N = int(input())

M = int(input())

dic = {}
for i in range(N):
    dic[i+1] = set()
for i in range(M):
    x, y = map(int,sys.stdin.readline().split())
    dic[x].add(y)
    dic[y].add(x)

visited = set()
dfs(dic, 1)
print(dic, visited)
print(len(visited)-1)