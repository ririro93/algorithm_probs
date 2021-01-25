from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

## 일단 그냥 k에 대해 loop 돌려서 시간초과 나오는거 경험해보기 -> 7% 에서 시간초과ㅎㅎ
# inputs -> things = [[2, 7, 1], [1, 9, 3]]
N, M = map(int, input().split())
things = [list(map(int, input().split())) for _ in range(N)]

# init
cache = [0] * (M+1)

# exe
for thing in things:
    # V: 무게, C: 만족도, K: 개수
    V, C, K = thing
    for i in range(M, V-1, -1):
        # tmp는 cache[i] 값 구하기 위해 무게 K 전꺼, 2K 전꺼, ... 확인하는거
        # i - V*num >= 0 야됨
        # 
        num = 0
        while i - V*num >= 0 and num <= K:
            cache[i] = max(cache[i], cache[i-V*num] + C*num)
            num += 1
        # print(i, cache)
print(cache[-1])