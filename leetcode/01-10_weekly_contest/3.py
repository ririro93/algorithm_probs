# inputs
source = [1, 2, 3, 4]
target = [2, 1, 4, 5]
allowedSwaps = [[0,1],[2,3]]

# function 
def DFS(start):    
    visited[start] = True
    result.append(start)
    for goal in G[start]:
        if visited[goal]:
            continue
        DFS(goal)
    

# init
l = len(source)
G = [[] for _ in range(l)]
print(G)

for swap in allowedSwaps:
    a, b = swap
    G[a].append(b)
    G[b].append(a)

visited = [False for _ in range(l)]
loops = []
nomis = [[] for _ in range(l)]

# exe
for i, g in enumerate(G):
    if g:
        if visited[i]:
            continue
        result = []
        DFS(i)
        loops.append(result)
        
print(loops)
for i in range(l):
    for loop in loops:
        if i in loop:
            for j in loop:
                nomis[i].append(source[j])
print(nomis)

total = l
for i in source:
    if i in nomis[i]:
        l -= 1
        
print(total)