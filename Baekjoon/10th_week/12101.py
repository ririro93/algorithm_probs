from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N, K = map(int, input().split())

# init
dic = {
    1: ['1'],
    2: ['1+1', '2'],
    3: ['1+1+1', '1+2', '2+1', '3']
}

# exec
for i in range(4, N+1):
    result = []
    for a in dic[i-1]:
        result.append('1' + '+' + a)

    for a in dic[i-2]:
        result.append('2' + '+' + a)

    for a in dic[i-3]:
        result.append('3' + '+' + a)
    dic[i] = result

if K > len(dic[N]):
    print(-1)
else:
    print(dic[N][K-1])