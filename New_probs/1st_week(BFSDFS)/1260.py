############################################################## DFS와 BFS
from collections import deque
from copy import deepcopy


# inputs
N, M, V = map(int, input().split())

lines = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    lines[i][j] = 1
    lines[j][i] = 1
    
linesB = deepcopy(lines)

# functions
def DFS(start, given_list, checked=[]):
    checklist = given_list
    deq = deque()
    deq.append(start)
    path = []
    
    while deq:
        point = deq.popleft()
        if point not in path:
            path.append(point)
        for goal in range(N, 0, -1):
            if checklist[point][goal] == 1:
                checklist[point][goal] = 0
                checklist[goal][point] = 0
                deq.appendleft(goal)
    return path

def BFS(start, given_list):
    checklist = given_list
    deq = deque()
    deq.append(start)
    path = [start]
    
    while deq:
        point = deq.popleft()
        for goal in range(1, N+1):
            if checklist[point][goal] == 1 and goal not in path:
                checklist[point][goal] = 0
                checklist[goal][point] = 0
                deq.append(goal)
                path.append(goal)
    return path

# exe
print(*DFS(V, lines))
print(*BFS(V, linesB))