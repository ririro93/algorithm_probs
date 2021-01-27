from sys import stdin

stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
R, C = map(int, input().split())
G = [[*input().strip()] for _ in range(R)]

# function
def check(R, C):
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for r in range(R):
        for c in range(C):
            if  G[r][c]== 'W':
                for d in dirs:
                    nr = r + d[0]
                    nc = c + d[1]
                    if 0 <= nr < R and 0 <= nc < C:
                        if G[nr][nc] == 'S':
                            return 0
                        elif G[nr][nc] == '.':
                            G[nr][nc] = 'D'
    return 1

# exe
result = check(R, C)
if result:
    print(result)
    for r in range(R):
        print(*G[r], sep='')
else:
    print(result)
