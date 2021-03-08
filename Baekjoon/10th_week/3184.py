from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# functions
def BFS(i, j):
    # init
    stack = [[i, j]]
    checked[i][j] = True
    sheeps = 0
    wolves = 0
    
    
    while stack:
        r, c = stack.pop()
        if G[r][c] == 'o':
            sheeps += 1
        elif G[r][c] == 'v':
            wolves += 1
            
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C and not checked[nr][nc] and G[nr][nc] != '#':
                stack.append([nr, nc])
                checked[nr][nc] = True
                
    if sheeps > wolves:
        return sheeps, 0
    else:
        return 0, wolves
    

# inputs
R, C = map(int, input().split())
G = [input().rstrip() for _ in range(R)]

# init
checked = [[False] * C for _ in range(R)]
sheeps_total = wolves_total = 0

# exec
for i in range(R):
    for j in range(C):
        if not checked[i][j] and G[i][j] != '#':
            s, w = BFS(i, j)
            sheeps_total += s
            wolves_total += w
print(sheeps_total, wolves_total)