from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# 동적 계획법으로 다시 풀어보기
# 모든 물건은 넣거나 말거나 두가지 경우의 수 밖에 없다

# inputs
N, K = map(int, input().split())

# init
cache = [0] * (K+1)

## exe
# 각 물건을 넣거나 말 때 각 무게에 대해 최대 가치 값을 구한다
for _ in range(N):
    W, V = map(int, input().split())
    # 무게가 K 일때는 기존의 K일때의 최대 가치와 K- W 중 큰 값을 저장한다
    for i in range(K, W-1, -1):
        cache[i] = max(cache[i], cache[i-W] + V)
print(cache[-1])
        
        
    