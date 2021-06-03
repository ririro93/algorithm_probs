from sys import stdin
from heapq import heapify, heappush, heappop

# stdin = open('inputs.txt', 'r')
input = stdin.readline

## 파일 합치기 3
T = int(input())

for _ in range(T):
    # init
    K = int(input())
    files = list(map(int, input().split()))
    heapify(files)
    result = 0

    # exec
    while len(files) > 1:
        file1 = heappop(files)
        file2 = heappop(files)
        heappush(files, file1+file2)
        result += file1 + file2
    print(result)