from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())

# exe
for _ in range(N):
    A, B = input().strip().split()
    dicA = {}
    dicB = {}
    for a in A:
        dicA[a] = dicA.get(a, 0) + 1
    for b in B:
        dicB[b] = dicB.get(b, 0) + 1
    for k, v in dicA.items():
        if v != dicB.get(k, 0):
            print('Impossible')
            break
    else:
        print('Possible')