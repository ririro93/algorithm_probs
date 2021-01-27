from collections import deque
import time


# initialization -> qu: current available positions, nqu: next available positions
knight_moves = [[2, 1],
                [1, 2],
                [2, -1],
                [1, -2],
                [-2, -1],
                [-1, -2],
                [-2, 1],
                [-1, 2]]

# get inputs -> s: start, f: finish, n: new
N = int(input())
size, sx, sy, fx, fy = [0]*N, [0]*N, [0]*N, [0]*N, [0]*N


for i in range(N):
    size[i] = int(input())
    sx[i], sy[i] = map(int, input().split(' '))
    fx[i], fy[i] = map(int, input().split(' '))

start_time = time.time()
####################################################################
# execution
for i in range(N):  
    finished = False
    if [sx[i], sy[i]] == [fx[i], fy[i]]:
        print(0)
        finished = True
    else:
        qu = deque()
        board = [[0]* size[i] for _ in range(size[i])]
        checked = [[False] * size[i] for _ in range(size[i])]
        qu.append([sx[i], sy[i]])
        
        while not finished:
            x, y = qu.popleft()
            checked[x][y] = True
            directions = []
            if fx[i] - x > 0:
                directions = knight_moves[:4]
            elif fx[i] - x < 0:
                directions = knight_moves[4:]
            else:
                directions = knight_moves[:]
                
            for direction in directions:
                # print("direction: ", direction)
                nx = x + direction[0]
                ny = y + direction[1]
                # print("nx: ", nx)
                if [nx, ny] == [fx[i], fy[i]]:
                    print(board[x][y]+1)
                    finished = True
                elif nx >= 0 and ny >= 0 and nx < size[i] and ny < size[i]:
                    # first visit to square
                    if board[nx][ny] == 0 and not checked[nx][ny]:
                        qu.append([nx, ny])
                        # print("qu: ", qu)
                        board[nx][ny] = board[x][y] + 1
                        checked[nx][ny] = True
####################################################################
# print("time: ", time.time() - start_time)