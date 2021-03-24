from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
S = input().rstrip()

# init
counts = {}
for i in range(1, 9):
    counts[str(i)] = 0
counts['zero'] = 0
ans = 0

# exec
for s in S:
    if s == '0':
        counts['zero'] += 1
    elif s == '9':
        counts['6'] += 1
    else:
        counts[s] += 1

for key, val in counts.items():
    if key == '6':
        q, r = divmod(val, 2)
        if r:
            q += 1
        ans = max(ans, q)
    else:
        ans = max(ans, val)
print(ans) 

