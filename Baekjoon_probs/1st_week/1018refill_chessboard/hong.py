def count_sq(y, x):
    color = ['W', 'B']
    s1 = 0
    for i in range(y, y+8):
        for j in range(x, x+8):
            if board[i][j] != color[(i+j)%2]:
                s1 += 1
    color = ['B', 'W']
    s2 = 0
    for i in range(y, y+8):
        for j in range(x, x+8):
            if board[i][j] != color[(i+j)%2]:
                s2 += 1
    return min(s1, s2)

n, m = map(int, input().split(' '))
board = []
for i in range(n):
    board.append([])
    line = input()
    for j in range(m):
        board[i].append(line[j])
        
        
M = 2**30
for i in range(n-7):
    for j in range(m-7):
        M = min(M, count_sq(i, j))
        
print(M)
        