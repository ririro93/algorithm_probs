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
def BFS(start, goal):
    cnt = 0
    checked.append(start)
    targets = [start]
    while True:
        new_targets = []
        for target in targets:
            for g in G[target]:
                if g == goal:
                    return cnt+1
                elif g in checked:
                    continue
                else:
                    checked.append(g)
                    new_targets.append(g)
        if new_targets:
            targets = new_targets[:]
        else:
            return -1
        cnt += 1
                
            
# init
checked = []

# exe
print(BFS(start, goal))