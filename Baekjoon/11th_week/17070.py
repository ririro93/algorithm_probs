from sys import stdin

stdin = open('input.txt', 'r')
input = stdin.readline

# functions
def DFS(start, end, curr):
    global N, result
    
    # print(end, curr)
    
    for move in dirs[curr]:
        nstart = end
        nend = [end[0]+move['dir'][0], end[1]+move['dir'][1]]
        ncurr = move['next']
        if nend == [N, N]:
            result += 1
            # print('goal')
            return
        if 0 <= nend[0] < N and 0 <= nend[1] < N:
            if ncurr in ['hor', 'ver'] and House[nend[0]][nend[1]] == 0:
                DFS(nstart, nend, ncurr)
            elif ncurr == 'diag' and House[nend[0]][nend[1]] == 0 and House[nend[0]-1][nend[1]] == 0 and House[nend[0]][nend[1]-1] == 0:
                DFS(nstart, nend, ncurr)
################################################################
# inputs
N = int(input())
House = [list(map(int, input().split())) for _ in range(N)]

# init
dirs = {
    'hor': [
        {'dir': [0, 1], 'next': 'hor'},
        {'dir': [1, 1], 'next': 'diag'}
    ],
    'ver': [
        {'dir': [1, 0], 'next': 'ver'},
        {'dir': [1, 1], 'next': 'diag'}
    ],
    'diag': [
        {'dir': [0, 1], 'next': 'hor'},
        {'dir': [1, 1], 'next': 'diag'},
        {'dir': [1, 0], 'next': 'ver'}
    ]
}
result = 0

# exec
DFS([0, 0], [0, 1], 'hor')
print(result)