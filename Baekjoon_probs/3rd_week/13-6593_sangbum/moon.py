from collections import deque

# # get inputs, initialization
# H: height, R: row, C: col
Heights = []
Rows = []
Cols = []
Buildings = []
starts = []
counts = 0
time_list = []
directions = [[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1],
              [-1, 0, 0],
              [0, -1, 0],
              [0, 0, -1]]

while True:
    H, R, C = map(int, input('').split(' '))
    if H == 0 and R == 0 and C == 0:
        break
    Heights.append(H)
    Rows.append(R)
    Cols.append(C)
    Buildings.append([[[0]*C for _ in range(R)] for _ in range(H)])
    for h in range(H):
        for i in range(R):
            Buildings[counts][h][i] = [*list(input(''))]
            if "S" in Buildings[counts][h][i]:
                starts.append([h, i, Buildings[counts][h][i].index("S")])
        _ = input('')
    counts += 1
            
# print("Heights: ", Heights)
# print("Rows: ", Rows)
# print("Cols: ", Cols)
# print("Buildings: ", Buildings)
# print("starts: ", starts)
            
          
# execution
for count in range(counts):
    checked = [[[False] * Cols[count] for _ in range(Rows[count])] for _ in range(Heights[count])]
    time = 0
    finished = False
    qu = deque()
    qu.append(starts[count])
    
    while qu and not finished:
        h, r, c = qu.popleft()
        
        for direction in directions:
            nh = h + direction[0]
            nr = r + direction[1]
            nc = c + direction[2]
            
            if nh >= 0 and nr >= 0 and nc >= 0 and nh < Heights[count] and nr < Rows[count] and nc < Cols[count]:
                # if finished
                if Buildings[count][nh][nr][nc] == "E":
                    time_list.append(time - 1)
                    finished = True
                elif not checked[nh][nr][nc] and Buildings[count][nh][nr][nc] == ".":
                    qu.append([nh, nr, nc])
                    checked[nh][nr][nc] = True
        time += 1
    if not finished:
        time_list.append("Trapped!")

for time in time_list:
    if type(time) == int:
        print("Escaped in {} minute(s).".format(time))
    else:
        print(time)
