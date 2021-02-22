from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())

# init
result = 0

# exec
for _ in range(N):
    # inputs
    S = input().strip()
    
    # init
    stack = []

    # exec
    for s in S:
        if stack:
            last = stack[-1]
            if s != last:
                stack.append(s)
            else:
                stack.pop()
        else:
            stack.append(s)
    if not stack:
        result += 1
print(result) 
            