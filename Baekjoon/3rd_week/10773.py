from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
K = int(input())
A = [int(input()) for _ in range(K)]

# init
stack = []

# exe
for a in A:
    if a:
        stack.append(a)
    else:
        stack.pop()
print(sum(stack))