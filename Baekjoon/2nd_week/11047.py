# from sys import stdin

# stdin = open('input.txt', 'r')
# input = stdin.readline

# inputs 
N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

# inits
left = K
cnt = 0

# exe
while left > 0:
    for a in A[::-1]:
        if a <= K:
            q, mod = divmod(left, a)
            cnt += q
            left = mod

print(cnt)
                    
    