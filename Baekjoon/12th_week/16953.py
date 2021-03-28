from sys import stdin
from collections import deque

# stdin = open('input.txt', 'r')
input = stdin.readline

# functions
def multi(a):
    return 2*a

def addOne(a):
    return 10*a + 1

def DFS(A, B):
    deq = deque([A])
    cnt = 0
    while deq:
        for _ in range(len(deq)):
            curr = deq.popleft()
            next1 = multi(curr)
            next2 = addOne(curr)
            if next1 == B or next2 == B:
                return cnt + 2
            if next1 < B:
                deq.append(next1)
            if next2 < B:
                deq.append(next2)
        cnt += 1
    return -1
            

################################
# inputs
A, B = map(int, input().split())

# exec
print(DFS(A, B))
