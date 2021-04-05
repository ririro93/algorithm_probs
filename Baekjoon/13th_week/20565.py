from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N, M = map(int, input().split())

# init
min_sides = N
max_sides = N * 6

# exec
# 주사위 수가 눈 수 보다 크면 적어도 한 주사위는 눈이 없다
if N > M:
    print(0)
else:
    q, r = divmod(M, N)
    print(((q**(N-r)) * ((q+1)**r)) / 6**N)

