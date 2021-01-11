import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

n,k = map(int,input().split())
cache = [1] + [0]*k

for value in [int(input())for _ in range(n)]:
    for x in range(value,k+1):
        cache[x] += cache[x-value]
        print(cache)
print(cache[-1])