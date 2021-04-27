from sys import stdin, setrecursionlimit

# stdin = open('input.txt', 'r')
input = stdin.readline

setrecursionlimit(10**7)

# functions
def find_cycle(curr, former, order):
    global done

    if done:
        return
    for n_node in G[curr]:
        if not checked[n_node]:
            checked[n_node] = True
            find_cycle(n_node, curr, order + [n_node])
            if done:
                return
            checked[n_node] = False
        # 직전에 지난 역이 아닌데 이미 지나간 역이면 싸이클이 있는거다
        elif checked[n_node] and n_node != former:
            done = True
            idx = order.index(n_node)
            for n in order[idx:]:
                is_cycle.append(n)
            return

def find_distances(start):
    n_checked = [False] * (N+1)

    n_checked[start] = True
    stack = [start]


    while stack:
        curr = stack.pop()
        for n_node in G[curr]:
            if not n_checked[n_node]:
                if distances[n_node] == 1000:
                    distances[n_node] = distances[curr] + 1
                n_checked[n_node] = True
                stack.append(n_node)
            
########################################
# inputs
N = int(input())
G = [[] for _ in range(N+1)]
for _ in range(N):
    s, e = map(int, input().split())
    G[s].append(e)
    G[e].append(s)

# init
checked = [False] * (N+1)
done = False
distances = [1000] * (N+1)        # 사이클에서 인덱스 역까지 거리
is_cycle = []

## exec
# 사이클 찾기
checked[1] = True
find_cycle(curr=1, former=0, order=[1])
for node in is_cycle:
    distances[node] = 0

# 사이클에 속한 첫 원소 찾기
for i in range(1, N+1):       
    if distances[i] == 0:
        start = i
        break

# 사이클에 속한 아무 역에서 시작해서 DFS 하면서 모든 거리 구하기
find_distances(start)          
print(*distances[1:])