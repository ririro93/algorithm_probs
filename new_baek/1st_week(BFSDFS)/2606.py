# inputs
N = int(input())
M = int(input())

g = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

# init
checked = [False for _ in range(N+1)]

# functions
def DFS():
    cnt = 0
    stack = [1]
    checked[1] = True
    while stack:
        goal = stack.pop()
        for next_point in g[goal]:
            if not checked[next_point]:
                stack.append(next_point)
                checked[next_point] = True
                cnt += 1
    return cnt

# exe
print(DFS())
    
    