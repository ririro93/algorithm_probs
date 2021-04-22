from sys import stdin

stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())

# init
G = []
start = '*'*N + ' '*(2*N-3) + '*'*N

# exec
G.append(start)
for i in range(1, N):
    mid = (N-1) * ' ' + '*' + ' '*(N-2) + '*' + ' '*(N-2) + '*' + (N-1) * ' '
    G.append(mid)
G.append(start)

for g in G:
    print(g)
    