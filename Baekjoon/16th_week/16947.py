from sys import stdin

stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())
Stops = [list(map(int, input().split())) for _ in range(N)]
