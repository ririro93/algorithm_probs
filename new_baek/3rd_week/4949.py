from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# function
def solve(S):
    stack = [1]
    
    for s in S:
        if s == '(':
            stack.append('(')
        if s == ')':
            if stack.pop() != '(':
                return 'no'
        if s == '[':
            stack.append('[')
        if s == ']':
            if stack.pop() != '[':
                return 'no'
    if stack == [1]:
        return 'yes'
    else:
        return 'no'

# exe
while True:
    S = input().rstrip()
    if S == '.':
        break
    print(solve(S))