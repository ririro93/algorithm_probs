from sys import stdin

stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
K = int(input())

# functions
def Bi(G):
    checked = []
    stack = []
    cnt = 0
    
    for i, g in enumerate(G):
        if g and i not in checked:
            checked.append(i)
            stack.append(i)
            cnt += 1
        while stack:
            print("stack: ", stack)
            print("checked: ", checked, "\n")
            l = len(stack)
            points = []
            for _ in range(l):
                points.append(stack.pop())
            for point in points:
                if point not in checked:
                    checked.append(point)
                for ele in G[point]:
                    if ele not in checked:
                        stack.append(ele)
    return cnt
                    
            
            
                
    
     

# exe
for _ in range(K):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    
    for _ in range(E):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    print(G)
    print(Bi(G))