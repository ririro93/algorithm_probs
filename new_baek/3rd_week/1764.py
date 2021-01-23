from sys import stdin
stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N, M = map(int, input().split())

# init
dic = {}
ans = []
# exe
for _ in range(N):
    hear = input().strip()
    dic[hear] = 1

for _ in range(M):
    see = input().strip()
    if see in dic:
        ans.append(see)

print(len(ans))
print(*sorted(ans), sep='\n')
    
    
