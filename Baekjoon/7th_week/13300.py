from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N, K = map(int, input().split())

# init
students = [[0]*7 for _ in range(2)]
for _ in range(N):
    S, Y = map(int, input().split())
    students[S][Y] += 1
cnt = 0

# exec
for sex in students:
    for s in sex:
        q, r = divmod(s, K)
        cnt += q
        cnt = cnt+1 if r else cnt
print(cnt) 
    
    
