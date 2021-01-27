from collections import deque

# inputs
N, M = map(int, input().split())
g = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

# print(g)

# number of nodes with no connections
cnt = -1 

for row in g:
    if row == []:
        cnt += 1

    
# init
checked = [False for _ in range(N+1)]

# functions
def BFS():
    global cnt
    deq = deque()
    
    for i in range(1, N+1):
        if g[i] and not checked[i]:
            deq.append(i)
            checked[i] = True
            while deq:
                start = deq.pop()
                for dest in g[start]:
                    if not checked[dest]:
                        deq.append(dest)
                        checked[dest] = True                
            cnt += 1
    return cnt

print(BFS())
                

    

