from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())
A = list(map(int, input().split()))

# init
total = 0
S = sum(A)
S2 = 0

# exe
A.sort()
for i in range(len(A) - 1):
    S -= A[i]
    total += A[i] * S 
print(total)


