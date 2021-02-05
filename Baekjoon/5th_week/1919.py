from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
A = input().strip()
B = list(input().strip())

# init
cnt = 0

# exe
for a in A:
    if a in B:
        B.remove(a)
    else:
        cnt += 1
print(cnt+len(B))