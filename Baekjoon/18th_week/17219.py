from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N, M = map(int, input().split())
Infos = [list(input().split()) for _ in range(N)]
Sites = [input().rstrip() for _ in range(M)]

# init
dic = {}
for address, pw in Infos:
    new_add = address.replace('.', 'dot').replace('-', 'dash')
    dic[new_add] = pw

# exec
for site in Sites:
    new_site = site.replace('.', 'dot').replace('-', 'dash')
    print(dic[new_site])