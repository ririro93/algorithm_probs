from collections import deque
from sys import stdin, exit

directions = [[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1],
              [-1, 0, 0],
              [0, -1, 0],
              [0, 0, -1]]

while True:
    # # get inputs, initialization
    # H: height, R: row, C: col
    H, R, C = map(int, stdin.readline().strip().split(' '))

    if H == 0 and R == 0 and C == 0:
        exit()

    Building = [[[0]*C for _ in range(R)] for _ in range(H)]
    for h in range(H):
        for i in range(R):
            Building[h][i] = [*list(stdin.readline().strip())]
            if "S" in Building[h][i]:
                start = [h, i, Building[h][i].index("S")]          
        _ = stdin.readline()
            
    # execution
    checked = [[[False] * C for _ in range(R)] for _ in range(H)]
    time = 0
    finished = False
    qu = deque()
    qu.append(start)

    while qu and not finished:
        h, r, c = qu.popleft()
        if Building[h][r][c] == "S":
            Building[h][r][c] = 0

        for direction in directions:
            nh = h + direction[0]
            nr = r + direction[1]
            nc = c + direction[2]

            if nh >= 0 and nr >= 0 and nc >= 0 and nh < H and nr < R and nc < C:
                # if finished
                if Building[nh][nr][nc] == "E":
                    time = Building[h][r][c] + 1
                    finished = True
                elif not checked[nh][nr][nc] and Building[nh][nr][nc] == ".":
                    qu.append([nh, nr, nc])
                    checked[nh][nr][nc] = True
                    Building[nh][nr][nc] = Building[h][r][c] + 1
    if not finished:
        print("Trapped!")
    else:
        print("Escaped in {} minute(s).".format(time))
