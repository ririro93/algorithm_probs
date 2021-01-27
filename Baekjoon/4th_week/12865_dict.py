from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline 

# inputs
N, K = map(int, input().split())

# init -> 무게 0 일때 가능한 최대가치 0 으로 가방 초기화
bag = {0:0}

# exe
for _ in range(N):
    W, V = map(int, input().split())
    tmp = {}
    # 전에 고려해본 모든 무게들에 대해서만 새 물품 넣었을 때 가치 높아지나 확인
    for key, val in bag.items():
        nW = W + key
        nV = V + val
        if nW > K:
            continue
        tmp[nW] = max(bag.get(nW, 0), nV)
        max_val = max(max_val, tmp[nW])
    # 충돌 일어나지 않게 tmp에 저장했다가 한번에 업데이트
    bag.update(tmp)
print(max_val)
# print(max(bag.values()))