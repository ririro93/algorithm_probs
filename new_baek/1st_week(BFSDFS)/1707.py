# from sys import stdin

# stdin = open('input.txt', 'r')
# input = stdin.readline

# inputs
K = int(input())

# functions
def Bi(G, color):
    V_color = True
    stack = []
    # print(G)
    for i, g in enumerate(G):
        if g and not color[i]:
            color[i].append(V_color)
            V_color = not V_color
            stack.append(i)
                            
            while stack: 
                # print("stack: ", stack)
                # print("color: ", color)
                # print("V_color: ", V_color, "\n")
                points = []
                stack_l = len(stack)
                for _ in range(stack_l):
                    points.append(stack.pop())
                for point in points: 
                    for ele in G[point]: 
                        if not color[ele]:
                            color[ele].append(V_color)
                            stack.append(ele)
                            # points에 넣고 마지막에 stack = points 로 바꿔치기하면 훨 편함
                        else:
                            if color[ele][0] != V_color:
                                # print("ele: ", ele)
                                return "NO"
                V_color = not V_color
    return "YES"                

# exe
for _ in range(K):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    color = [[] for _ in range(V+1)]
    
    for _ in range(E):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    if V <= 2 or E <= 2:
        print("YES")
    else:
        print(Bi(G, color))