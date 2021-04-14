from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

## 1138: 한줄로 서기
# inputs
N = int(input())
A = list(map(int, input().split()))

# init
result = [N]

# exec
for i in range(N-1, 0, -1):
    result = result[:A[i-1]] + [i] + result[A[i-1]:]
print(*result)
