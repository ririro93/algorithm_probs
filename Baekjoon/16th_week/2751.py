from sys import stdin

stdin = open('input.txt', 'r')
input = stdin.readline

## 2751. 수 정렬하기 2
# inputs
N = int(input())

# init
nums = list(int(input()) for _ in range(N))
nums.sort()
for num in nums:
    print(num)