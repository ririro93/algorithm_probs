# 압축
# from sys import stdin

# # stdin = open('input.txt', 'r')
# input = stdin.readline

# inputs
# S = input().strip()
S = input()

# init
result = '0'

# exe
if len(S) == 1:
    result = '1'
else:
    for i, s in enumerate(S):
        if i >= len(S) - 2:
            if s.isdigit():
                result += '+1'
            elif s == '(':
                result += '*('
            elif s == ')':
                result += '+0)'
            continue
        if s.isdigit() and S[i+1] == '(':
            result += '+' + s
        elif s.isdigit():
            result += '+1'
        elif s == '(':
            result += '*('
        elif s == ')':
            result += '+0)'
# print(result)
print(eval(result))
