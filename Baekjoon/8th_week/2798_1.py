from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# functions
def solve(N, M, K, tmp):
    global total
    if K == 3:
        total = max(total, tmp)
    else:
        for i in range(N):
            if not checked[i]:
                if tmp + cards[i] > M:
                    continue
                else:
                    checked[i] = True
                    solve(N, M, K+1, tmp+cards[i])
                    checked[i] = False

# inputs
N, M = map(int, input().split())
cards = list(map(int, input().split()))

# init
checked = [False] * N
total = 0

# exec
solve(N, M, 0, 0)
print(total)