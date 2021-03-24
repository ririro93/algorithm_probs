from sys import stdin

stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
G = [list(map(int, input().split())) for _ in range(9)]

# init
checked_row = [[False] * 10 for _ in range(9)]
checked_col = [[False] * 10 for _ in range(9)]
checked_block = [[False] * 10 for _ in range(9)]

for i in range(9):
    for j in range(9):
        
        