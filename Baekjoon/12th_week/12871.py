from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
S = input().rstrip()
T = input().rstrip()

# init
S, T = S * len(T), T * len(S)

# exec
if S == T:
    print(1)
else:
    print(0)