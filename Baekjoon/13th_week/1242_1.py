from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N, K, M = map(int, input().split())

# init
if K > N:
    mul = (K-M) // N
    i = M + N*mul
else:
    i = M
length = N

# exec
while True:
    # print('i:', i, 'length:', length)
    if i == K:
        print(N-length+1)
        break
    if length == 1:
        print(N)
        break

    i -= K
    if i < 0:
        i += length
        x = (K-i) // (length-1)
        i += x*(length-1)
    length -= 1