from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
T = int(input())

# init
buttons = [300, 60, 10]
result = []

# exe
for button in buttons:
    q, r = divmod(T, button)
    result.append(q)
    T = r
if r:
    print(-1)
else:
    print(*result, sep=' ')


