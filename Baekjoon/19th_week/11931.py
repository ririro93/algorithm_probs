from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())
A = [int(input()) for _ in range(N)]

# init
A.sort(reverse=True)

# exec
for a in A:
    print(a)