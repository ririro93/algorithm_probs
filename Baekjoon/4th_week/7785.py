from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline 

# inputs
N = int(input())

# init
dic = {}

for _ in range(N):
    name, action = input().split()
    if action == 'enter':
        dic[name] = dic.get(name, 0) + 1
    else:
        dic[name] -= 1
        if dic[name] == 0:
            del dic[name]

result = []
for key, val in dic.items():
    result.append(key)
result = sorted(result, reverse=True)
print(*result, sep='\n')
        
