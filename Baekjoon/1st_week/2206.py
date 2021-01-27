from collections import deque
# from sys import stdin
 
# stdin = open('input.txt', 'r')
# input = stdin.readline
 
 
# init (padding added)
N, M = map(int, input().split())
G = [[2] * (M+1)] + [[2] +[*map(int, list(input().strip()))] for _ in range(N)]
checked0 = [[False for _ in range(M+1)] for _ in range(N+1)]
checked1 = [[False for _ in range(M+1)] for _ in range(N+1)]
dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]


# function -> 재귀로 해보기
def BFS(_start):
    cnt = 1
    deq = deque()
    deq.append((_start, 1))
    checked0[_start[0]][_start[1]] = True
    checked1[_start[0]][_start[1]] = True
    while deq:
        deq_len = len(deq)
        points = []
        cnt += 1
        for _ in range(deq_len):
            points.append(deq.popleft())
        # print("\npoints: ", points)
        for ([x, y], wall_break) in points:
            for d in dirs:
                nx = x + d[0]
                ny = y + d[1]
                if nx == N and ny == M:
                    return cnt
                elif 1 <= nx <= N and 1 <= ny <= M:
                    if G[nx][ny] == 0 and wall_break and not checked1[nx][ny]:
                        checked1[nx][ny] = True
                        deq.append(([nx, ny], wall_break))
                    elif G[nx][ny] == 0 and not wall_break and not checked0[nx][ny]:
                        checked0[nx][ny] = True
                        deq.append(([nx, ny], wall_break))
                    elif G[nx][ny] == 1 and wall_break and not checked1[nx][ny]: 
                        checked1[nx][ny] = True
                        deq.append(([nx, ny], wall_break-1))
        # print("cnt: ", cnt, "deq: ", deq)    
    return -1
if N == 1 and M == 1:
    print(1)
else:
    print(BFS([1, 1]))
    