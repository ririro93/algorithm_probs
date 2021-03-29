from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N, K, M = map(int, input().split())

# init
i = 0
arr = list(range(1, N+1))
cnt = 0
# exec
while True:
    cnt += 1
    i += K-1
    i %= len(arr)
    curr = arr.pop(i)
    # print('i:', i, 'arr:', arr, 'curr:', curr)
    print(curr)
    if curr == M:
        print(cnt)
        break