from sys import stdin
from collections import deque

stack = deque()

for _ in range(int(stdin.readline())):
    command = stdin.readline().split()
    if command[0] == "push":
        stack.append(command[1])
    if command[0] == "pop":
        if stack: print(stack.pop())
        else: print(-1)
    if command[0] == "size":
        if stack: print(len(stack))
        else: print(0)
    if command[0] == "empty":
        if stack: print(0)
        else: print(1)
    if command[0] == "top":
        if stack: print(stack[len(stack) -1 ])
        else: print(-1)