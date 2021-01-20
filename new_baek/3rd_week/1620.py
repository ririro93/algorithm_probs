from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline


# inputs
N, M = map(int, input().split())
poke = []
for _ in range(N):
    poke.append(input().strip())

# exe
for _ in range(M):
    Q = input().strip()
    if Q.isdigit():
        print(poke[int(Q)-1])
    else:
        print(poke.index(Q)+1)