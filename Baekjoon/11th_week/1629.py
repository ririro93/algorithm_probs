from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# functions
def recur(a, b):
    global C
    if b == 1:
        return a % C
    else:
        if b % 2 == 0:
            return (recur(a, (b//2)) ** 2) % C
        else:
            return (recur(a, b//2) ** 2) * a % C
            
# inputs
A, B, C = map(int, input().split())

# exec
print(recur(A, B))
    