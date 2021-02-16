from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())
A = map(int, input().split())
M = int(input())
B = map(int, input().split())

# init
dictA = {}
for a in A:
    dictA[a] = 1

for b in B:
    print(dictA.get(b, 0))
