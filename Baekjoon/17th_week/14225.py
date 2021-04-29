from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())
S = list(map(int, input().split()))

# init
checked = set([0])

# exec
for num in S:
    tmp = set()
    for c in checked:
        tmp.add(c+num)
    checked |= tmp
result = list(checked)
result.sort()

i = 0
for ele in result:
    if ele != i:
        print(i)
        break
    i += 1
else:
    print(result[-1]+1)