from sys import stdin
import math

# stdin = open('input.txt', 'r')
input = stdin.readline

# input
N = int(input())

# function
def solve(N):
    digits = int(math.log(N, 10)) + 1
    target = N - 9 * digits
    for x in range(target, N):
        if x < 10:
            result = 2 * x
        else:
            result = x + sum(map(int, str(x)))
        if result == N:
            return x
    return 0

# exe
print(solve(N))
