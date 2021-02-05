from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

S = input().strip()
cnt = S.count(' ')
if cnt:
    print(cnt+1)
else:
    for s in S:
        if s != ' ':
            print(1)
            break
    else:
        print(0)