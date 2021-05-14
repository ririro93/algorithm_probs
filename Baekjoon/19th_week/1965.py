from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())
A = list(map(int, input().split()))

# init
result = [1] * N

# exec
if N == 1:
    print(result[0])
else:
    for i in range(1, N):
        max_val = 1
        for j in range(i-1, -1, -1):
            if A[i] > A[j]:
                max_val = max(max_val, result[j] + 1)
                break
        result[i] = max_val
    print(max(result))
