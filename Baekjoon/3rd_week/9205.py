from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
T = int(input())

# function -> 1 beer every 50m, 20 bottles max, return 'happy' or 'sad'
def happy(home, stores, dest, N):
    stack = [home]
    checked = [home]
    while stack:
        start = stack.pop()
        checked.append(start)
        for store in stores:
            # check distance to destination
            if abs(start[0] - dest[0]) + abs(start[1] - dest[1]) <= 1000:
                return 'happy'
            if store in checked:
                continue
            d = abs(store[0] - start[0]) + abs(store[1] - start[1])
            # check distance to other stores
            if d <= 1000:
                stack.append(store)
    return 'sad'

# exe
for _ in range(T):
    N = int(input())
    home = list(map(int, input().split()))
    stores = []
    for _ in range(N):
        stores.append(list(map(int, input().split())))
    dest = list(map(int, input().split()))
    
    if N == 0:
        if abs(home[0] - dest[0]) + abs(home[1] - dest[1]) <= 1000:
            print('happy')
        else:
            print('sad')
    else:
        print(happy(home, stores, dest, N))