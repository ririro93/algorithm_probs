from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())
heights = list(map(int, input().split()))

# init
heights.sort()
dic = {}
cnt = 0

# exec
for h in heights:
    if h > 0:
        if dic.get(h-1, 0) == 0:
            print(0)
            break
        
    dic[h]  = dic.get(h, 0) + 1
    
    if dic[h] == 2 and h > 0:
        if dic[h-1] < 2:
            print(0)
            break
        
    if dic[h] == 3:
        print(0)
        break
else:
    for key, val in dic.items():
        if  val == 2:
            cnt += 1
        if val == 1:
            cnt += 1
            break
    print(2 ** cnt)