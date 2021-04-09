from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())
nums = input().split()
M = int(input())
questions = input().split()

# init
dic = {}

# exec
for num in nums:
    dic[num] = dic.get(num, 0) + 1

for i in range(M):
    if i == M-1:
        print(dic.get(questions[i], 0), end='')
    else:
        print(dic.get(questions[i], 0), end=' ')