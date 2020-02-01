import time, random

#BOJ 7576: 토마토
input_1 = input()
m = int(input_1.rsplit()[0]) #가로
n = int(input_1.rsplit()[1]) #세로
box = []
visited = []
days = 0 #final result
ripe_original = [] # 전날에 익은 토마토
ripe_new = [] # 옆의 토마토 때문에 새롭게 익은 토마토
not_ripe = 0

for i in range(0, n):
    box.append([])
    visited.append([])
    row_input = input().rsplit()
    for j in range(0, m):
        box[i].append(int(row_input[j]))
        visited[i].append(False)
        if int(row_input[j]) == 1:
            ripe_original.append([i, j])
            visited[i][j] = True
        elif int(row_input[j]) == 0:
            not_ripe += 1
# m, n = 500, 500
# box = [[random.randint(0, 1)] * m for _ in range(n)]
# visited = [[False] * m for _ in range(n)]
start_time = time.time()
############################################################
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            ripe_original.append([i, j])
            visited[i][j] = True

while len(ripe_original) > 0:
    x, y = ripe_original.pop()
    #print("Visit " + str(x) + "," + str(y))
    if x > 0:
        if box[x-1][y] == 0 and not visited[x-1][y]:
            ripe_new.append([x-1, y])
            visited[x-1][y] = True
            box[x-1][y] = 1
            not_ripe -= 1
            #print("Affecting " + str(x-1) + "," + str(y))
    if y > 0:
        if box[x][y-1] == 0 and not visited[x][y-1]:
            ripe_new.append([x, y-1])
            visited[x][y-1] = True
            box[x][y-1] = 1
            not_ripe -= 1
            #print("Affecting " + str(x) + "," + str(y-1))
    if x < n-1:
        if box[x+1][y] == 0 and not visited[x+1][y]:
            ripe_new.append([x+1, y])
            visited[x+1][y] = True
            box[x+1][y] = 1
            not_ripe -= 1
            #print("Affecting " + str(x+1) + "," + str(y))
    if y < m-1:
        if box[x][y+1] == 0 and not visited[x][y+1]:
            ripe_new.append([x, y+1])
            visited[x][y+1] = True
            box[x][y+1] = 1
            not_ripe -= 1
            #print("Affecting " + str(x) + "," + str(y+1))
    if len(ripe_original) == 0:
        #print("ripe_new: " + str(ripe_new))
        ripe_original += ripe_new
        if len(ripe_new) > 0:
            days += 1
        ripe_new = []

if not_ripe > 0:
    print(-1)
else:
    print(days)
    
print('time: ', time.time() - start_time)