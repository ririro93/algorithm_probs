from sys import stdin
import math

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())

# init
G = []
G.append([['*']])
K = math.ceil(math.log(N, 3))

# exec
for i in range(K):
    base = G[-1]
    tmp = []
    for row in base:
        tmp.append(row*3)
    for row in base:
        tmp.append(row+[' ']*len(row)+row)
    for row in base:
        tmp.append(row*3)
    G.append(tmp)

for row in G[-1]:
    print(''.join(row))
        