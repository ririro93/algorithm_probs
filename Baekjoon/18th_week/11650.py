from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())
Coords = [list(map(int, input().split())) for _ in range(N)]

# exec
Coords.sort(key=lambda x: [x[0], x[1]])
for coord in Coords:
    print(*coord)