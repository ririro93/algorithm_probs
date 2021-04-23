from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# functions
def DFS(a, b, c):
    global A, B, C
    if [a, b, c] in checked:
        return
    
    checked.append([a, b, c])

    if a == 0:
        results.add(c)

    if a > 0:
        if b != B and [a - min(a, (B-b)), b + min(a, (B-b)), c] not in checked:
            DFS(a - min(a, (B-b)), b + min(a, (B-b)), c)
        if c != C and [a - min(a, (C-c)), b, c + min(a, (C-c))] not in checked:
            DFS(a - min(a, (C-c)), b, c + min(a, (C-c))) 
    if b > 0:
        if a != A and [a + min(b, (A-a)), b - min(b, (A-a)), c] not in checked:
            DFS(a + min(b, (A-a)), b - min(b, (A-a)), c)
        if c != C and [a, b - min(b, (C-c)), c + min(b, (C-c))] not in checked:
            DFS(a, b - min(b, (C-c)), c + min(b, (C-c))) 
    if c > 0:
        if a != A and [a + min(c, (A-a)), b, c - min(c, (A-a))] not in checked:
            DFS(a + min(c, (A-a)), b, c - min(c, (A-a)))
        if b != B and [a, b + min(c, (B-b)), c - min(c, (B-b))] not in checked:
            DFS(a, b + min(c, (B-b)), c - min(c, (B-b))) 

# inputs
A, B, C = map(int, input().split())

# init
checked = []
results = set()

# exec
DFS(0, 0, C)
results = list(results)
results.sort()
print(*results)