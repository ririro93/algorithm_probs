from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())
bars = [0] * 1001
start, end = 1000, 0                       
tallest = 0
for _ in range(N):
    L, H = map(int, input().split())
    bars[L] = H
    start, end = min(start, L), max(end, L)
    if H > tallest:
        tallest = H
        tallest_i = L

# init
total = 0

# exec
if N == 1:
    print(H)
else:
    tmp = bars[start]
    # start to tallest
    for i in range(start, tallest_i):
        tmp = max(tmp, bars[i])
        total += tmp
    
    # tallest
    total += tallest
    
    # end to tallest
    tmp = bars[end]
    for i in range(end, tallest_i, -1):
        tmp = max(tmp, bars[i])
        total += tmp
    print(total)
    
    
        
    
        
            
        