from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N, M = map(int, input().split())
cards = list(map(int, input().split()))

# init
final = 0

# exec
for i in range(7, 1 << N):
    cnt = 0
    sub_sum = 0
    for j in range(N):
        if i & (1 << j):
            cnt += 1
            sub_sum += cards[j]
        if cnt > 3 or sub_sum > M:
            break
    if cnt == 3:
        final = max(final, sub_sum)
print(final)