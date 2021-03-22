from sys import stdin
from itertools import combinations

# stdin = open('input.txt', 'r')
input = stdin.readline

# functions
def getDistance(house, chick):
    return abs(house[0] - chick[0]) + abs(house[1] - chick[1])

######################################################################
# inputs
N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]

# init
houses = []
chicks = []
for i in range(N):
    for j in range(N):
        if G[i][j] == 1:
           houses.append([i, j])
        elif G[i][j] == 2:
           chicks.append([i, j])
ans = []

# exec
combis = combinations(chicks, M)
for combi in combis:
    result = []
    for i in range(len(houses)):
        result.append(min([getDistance(houses[i], chick) for chick in combi]))
    ans.append(sum(result))
print(min(ans))