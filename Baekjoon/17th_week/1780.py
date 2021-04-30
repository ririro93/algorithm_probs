from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# functions
def is_all_same(rs, re, cs, ce):
    curr = G[rs][cs]
    for i in range(rs, re):
        for j in range(cs, ce):
            nxt = G[i][j]
            if nxt != curr:
                return False
    return True

def solve(rs, re, cs, ce):
    # 지금 보고 있는 부분이 다 같으면
    if is_all_same(rs, re, cs, ce):
        if G[rs][cs] == -1:
            results[0] += 1
        elif G[rs][cs] == 0:
            results[1] += 1
        else:
            results[2] += 1

    # 다른게 있으면 분활
    else:
        size = (re-rs) // 3
        for i in range(rs, re, size):
            for j in range(cs, ce, size):
                solve(i, i+size, j, j+size)

# inputs
N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]

# init
results = [0, 0, 0]

# exec
solve(0, N, 0, N)
for result in results:
    print(result)