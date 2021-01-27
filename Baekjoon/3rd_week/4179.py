from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs -> add padding to Graph
R, C = map(int, input().split())
G = [['#'] * (C+2)]
fires = []
for r in range(R):
    temp = [*input().rstrip()]
    G.append(['#'] + temp + ['#'])
    for c, val in enumerate(temp):
        if val == 'J':
            Joe = [r+1, c+1]
        elif val == 'F':
            fires.append([r+1, c+1])       
G.append(['#'] * (C+2))

# init
dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

# function
def BFS(fires, Joe, R, C):
    stack = [Joe]
    cnt = 1
    while stack:
        cnt += 1
        # get next positions of fires
        nfires = []
        for fire in fires:
            for d in dirs:
                nfire_r = fire[0] + d[0]
                nfire_c = fire[1] + d[1]
                if G[nfire_r][nfire_c] != '#' and G[nfire_r][nfire_c] != 'F':
                    G[nfire_r][nfire_c] = 'F'
                    nfires.append([nfire_r, nfire_c])   
                          
        # get Joe's next positions
        positions = []
        nstack = []
        l = len(stack)
        for _ in range(l):
            positions.append(stack.pop())
        for position in positions:
            for d in dirs:
                nr = position[0] + d[0]
                nc = position[1] + d[1]
                if G[nr][nc] == '.':
                    if nr == 1 or nr == R or nc == 1 or nc == C:
                        return cnt
                    G[nr][nc] = 'J'
                    nstack.append([nr, nc])
        stack = nstack[:]
        fires = nfires[:]
    return 'IMPOSSIBLE'
            
# exe
x, y  = Joe
if x == 1 or y == 1 or x == R or y == C:
    print(1)
else:
    print(BFS(fires, Joe, R, C))
