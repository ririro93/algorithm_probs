from collections import deque

# get inputs
N = int(input(''))
pic = [[*input('')] for _ in range(N)]

# initialization
checked = [[-1]*N for _ in range(N)]
qu = deque()
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
counterRG = 0
counterB = 0
counter = 0
# first: find (R, G), B 
for i in range(N):
    for j in range(N):
        # looking : current color
        looking = pic[i][j]
        if checked[i][j] == -1:
            qu.append([i, j])
            checked[i][j] = looking
            
            while qu:
                # print('qu: ', qu)
                # print('checked: ', checked)
                r, c = qu.popleft()
                for direction in directions:
                    nr = r + direction[0]
                    nc = c + direction[1]
                    if nr >= 0 and nc >= 0 and nr < N and nc < N:
                        if ((looking == "R" or looking == "G") and (pic[nr][nc] == "R" or pic[nr][nc] == "G") and checked[nr][nc] == -1):
                            checked[nr][nc] = looking
                            qu.append([nr, nc])
                        elif looking == "B" and pic[nr][nc] == "B" and checked[nr][nc] == -1:
                            checked[nr][nc] = looking
                            qu.append([nr, nc])  
            if looking == "R" or looking == "G":
                counterRG += 1
            elif looking == "B":
                counterB += 1
            
# second: find R, G
for i in range(N):
    for j in range(N):
        # looking : current color
        looking = pic[i][j]
        if checked[i][j] == "R" or checked[i][j] == "G":
            qu.append([i, j])
            checked[i][j] = "yes"
            
            while qu:
                # print('qu: ', qu)
                # print('checked: ', checked)
                r, c = qu.popleft()
                for direction in directions:
                    nr = r + direction[0]
                    nc = c + direction[1]
                    if nr >= 0 and nc >= 0 and nr < N and nc < N:
                        if pic[nr][nc] == looking and checked[nr][nc] != "yes":                  
                            checked[nr][nc] = "yes"
                            qu.append([nr, nc])
            counter += 1
print(counter+counterB)
print(counterRG+counterB)
        
        
