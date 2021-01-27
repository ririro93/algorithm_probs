from sys import stdin
from collections import deque

stdin = open('input.txt', 'r')
input = stdin.readline
n, k = map(int, input().split())

data = [len(input().strip()) for i in range(n)]
var = [0 for i in range(21)]
print(data)
print(var)
counter = 0

for i in range(n):
    if i > k:
        var[data[i-k-1]] -= 1
    counter += var[data[i]]
    var[data[i]] += 1
    print('i: ', i)
    print('var: ', var)
    print('counter: ', counter, '\n')
print(counter)