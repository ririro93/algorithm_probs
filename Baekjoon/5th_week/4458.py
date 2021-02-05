from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())

# function 
def capitalize(s):
    return s[0].upper()+s[1:]
# exe
for _ in range(N):
    print(capitalize(input().rstrip()))