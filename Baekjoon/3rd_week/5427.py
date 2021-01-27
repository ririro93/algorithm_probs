from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
T = int(input())

# init
dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

# function
def BFS(G, fires, start, W, H):
    stack = [start]
    cnt = 0
    # take out all possible positions at once and loop through
    while stack:
        cnt += 1
        
        # first get next fires
        n_fires = []
        for fire in fires:
            for d in dirs:
                nfire_x = fire[0] + d[0]
                nfire_y = fire[1] + d[1]
                if G[nfire_x][nfire_y] != '#' and G[nfire_x][nfire_y] != '*':
                    G[nfire_x][nfire_y] = '*'
                    n_fires.append([nfire_x, nfire_y])
        
        # next get my position
        l = len(stack)
        currs = []
        nexts = []
        for _ in range(l):
            currs.append(stack.pop())
            
        # my possible positions, don't add new position if overlapped with new fires
        for curr in currs:
            for d in dirs:
                nx = curr[0] + d[0]
                ny = curr[1] + d[1]
                # return if out of house
                if nx == 0 or nx == H + 1 or ny == 0 or ny == W + 1:
                    return cnt
                # if next position is room add to new positions
                if G[nx][ny] == '.':
                    nexts.append([nx, ny])
                    G[nx][ny] = 'x'               
                       
        # reset fires and my positions
        fires = n_fires
        stack = nexts
        
    return 'IMPOSSIBLE'
    

# exe
for _ in range(T):
    W, H = map(int, input().split())
    # add padding to Graph
    G = [['#']*(W+2)]
    fires = []
    for h in range(H):
        g = input().rstrip()
        G.append(['#'] + [*g] + ['#'])
        for w, c in enumerate(g):
            if c == '*':
                fires.append([h+1, w+1])
            elif c == '@':
                start = [h+1, w+1]
    G.append(['#']*(W+2))
    # for g in G:
    #     print(g)
    if W == 1 or H == 1:
        print(1)
        continue
    print(BFS(G, fires, start, W, H))