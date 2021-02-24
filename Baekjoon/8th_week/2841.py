from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N, P = map(int, input().split())
strings = [list(map(int, input().split())) for _ in range(N)]
# print(strings)

# init
total = 0
stacks = [[] for _ in range(7)]

# exec
for num, fret in strings:
    if not stacks[num]:
        stacks[num].append(fret)
        total += 1
    else:
        while stacks[num] and stacks[num][-1] > fret:
            stacks[num].pop()
            total += 1
        if stacks[num] and stacks[num][-1] == fret:
            continue
        stacks[num].append(fret)
        total += 1
print(total)