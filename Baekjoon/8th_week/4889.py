from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# init
i = 1

# inputs
while True:
    # inputs
    S = input().rstrip()
    if '-' in S:
        break
    # init
    cnt = 0
    total = 0
    
    # exec
    for s in S:
        if s == '{':
            total += 1
        elif s == '}':
            total -= 1
        
        if total < 0:
            total = 1
            cnt += 1
    print(f'{i}. {cnt + total//2}')
    i += 1