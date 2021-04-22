from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())

# exec
for i in range(1, N+1):
    print('*' * i)