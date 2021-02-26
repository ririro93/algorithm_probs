from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
S = input().rstrip()

# init
N = len(S)
start_float = N**0.5
if start_float > int(start_float):
    start = int(start_float) + 1
else:
    start = int(start_float)
for R in range(start, 0, -1):
    if N % R == 0:
        C = N // R
        if C >= R:
            break
tmp = [[] for _ in range(R)]
result = []

# exec
for i, s in enumerate(S):
    r = i % R
    tmp[r].append(s)

for row in tmp:
    result.extend(row)
print(''.join(result))    