from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())
S = list(map(int, input().split()))

# init
i = 0
step = S[i]
order = list(range(1, N+1))
right = True
result = []

for _ in range(N-1):
    result.append(order[i])
    order[i] = 0
    if step > 0:
        d = 1
    else:
        d = -1
    while step:
        i = (i+d) % N
        if order[i]:
            step -= d
    step = S[i]
result.append(order[i])
print(*result)


    