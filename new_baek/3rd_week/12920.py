from sys import stdin

stdin = open('input.txt', 'r')
input = stdin.readline

# inputs -> infos = [[2, 7, 1], [1, 9, 3]]
N, M = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(N)]

# init
max_value = sum([a*b for _, a, b in infos])
print(max_value)

# function

# exe