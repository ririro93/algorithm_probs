# 어떻게든 해볼라 했는데 이렇게 조건 하나하나 주다간 끝이 없을듯
# use as manay coins as possible 

from sys import stdin

stdin = open('input.txt')
input = stdin.readline

# inputs
P, C1, C2, C3, C4 = map(int, input().split())
C = [C1, C2, C3, C4] # [5, 3, 1, 2]
temp = C[:]

# init
coins = [1, 5, 10, 25]

# 