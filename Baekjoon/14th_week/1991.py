from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# functions
def preorder(curr):
    if curr:
        print(curr, end='')
        preorder(Tree[curr].get('left', False))
        preorder(Tree[curr].get('right', False))

def inorder(curr):
    if curr:
        inorder(Tree[curr].get('left', False))
        print(curr, end='')
        inorder(Tree[curr].get('right', False))

def postorder(curr):
    if curr:
        postorder(Tree[curr].get('left', False))
        postorder(Tree[curr].get('right', False))
        print(curr, end='')

# inputs
N = int(input())
nodes = [list(input().split()) for _ in range(N)]

# init
Tree = {}
for node in nodes:
    par = node[0]
    Tree[par] = {}

    left = node[1]
    right = node[2]
    if left != '.':
        Tree[par]['left'] = left
    if right != '.':
        Tree[par]['right'] = right

## exec
preorder('A')
print()
inorder('A')
print()
postorder('A')