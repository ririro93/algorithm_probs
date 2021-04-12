from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())

# init
ans = [
    ['*'],
]

# exec
for i in range(1, N+1):
    curr = ans[-1]
    new = curr[:]
    for j in range(2 ** (i-1)):
        new.append(curr[j] + ' ' * (2 ** (i-1) + j+1 - 2*len(curr[j])) + curr[j])
    ans.append(new)
for row in ans[-1][::-1]:
    print(row)
