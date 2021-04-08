from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())
inorder = list(map(int, input()))
postorder = list(map(int, input()))

# init
preorder = [0] * (N+1)

# exec
