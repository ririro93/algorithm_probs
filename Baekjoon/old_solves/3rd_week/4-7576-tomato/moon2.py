from collections import deque
import time
import random

# inputs -> N: num_row, M: num_col
M, N = map(int, input('').split(' '))
box = [[*map(int, input('').split(' '))] for _ in range(N)]

# # test inputs
# M, N = 500, 500
# box = [[random.randint(0, 1)] * M for _ in range(N)]
# start_time = time.time()
###################################################################
def add_new(qu_before, box, N, M, days):
    
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while qu_before:
        qu_after = []
        for v in qu_before:
            row, col = v[0], v[1]
            for direction in directions:
                nrow, ncol = [row+direction[0], col+direction[1]]
                if nrow >= 0 and ncol >= 0 and nrow < N and ncol < M:
                    if box[nrow][ncol] == 0:
                        qu_after.append((nrow, ncol))
                        box[nrow][ncol] = 1
        qu_before = qu_after
        days += 1
    return days - 1 

# execution
days = 0
qu_before = []
finished = False

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            qu_before.append((i, j))

days = add_new(qu_before, box, N, M, days)

for i in range(N):
    if 0 in box[i]:
        finished = True

if finished: print(-1)
else: print(days)
##############################################################################
# print('time: ', time.time() - start_time)

