from sys import stdin

stdin = open('input.txt', 'r')
input = stdin.readline

# exe
T = int(input())

for _ in range(T):
    N = int(input())
    cats = []
    names = [[] for _ in range(31)]
    cnt = 0
    result = 1
    
    for _ in range(N):
        name, cat = input().split()
        if cat in cats:
            if name not in names[cats.index(cat)]:
                names[cats.index(cat)].append(name)
        else:
            cats.append(cat)
            names[cnt].append(name)
            cnt += 1
            
    for i, c in enumerate(cats):
        result *= len(names[i]) + 1
        
    print(result - 1)
        
            