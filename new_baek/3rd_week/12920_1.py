from sys import stdin
from collections import deque

# stdin = open('input.txt', 'r')
input = stdin.readline

## cache[M] 값 하나 구할 때  M-V, M-2V, ... 도 한번에 같이 계산
# inputs -> things = [[2, 7, 1], [1, 9, 3]]
N, M = map(int, input().split())
things = [list(map(int, input().split())) for _ in range(N)]

# init
cache = [0] * (M+1)

# exe
for thing in things:
    # V: 무게, C: 만족도, K: 개수
    V, C, K = thing
    for i in range(M, M-V, -1): 
        # 이번 물건을 쓸수 있는 최대 개수부터 안쓰는거까지 생각하면서 값들 큐에 저장
        deq = deque()
        deq.append(0)
        point1 = 0 # 현재 최대값 가리키는 애
        point2 = 0 # 늙은애 없애는 용
        for num in range(M//V,  -1, -1):
            # 쓸려는 개수가 최대 개수보다 크면 최대개수까지만 주고
            # 쓸려는 개수가 현재 무게를 초과하면 안됨
            curr_weight = i - num*V
            possible_num = curr_weight // V
            if possible_num > K:
                possible_num = K
            # 덱에 물건 쓰기전 최대가치값이랑 물건 더하고 최대 가치값중 큰거 넣기
            deq.append(max(cache[curr_weight], cache[curr_weight-possible_num*V] + possible_num*C))
            # 새로 넣은게 기존 젤 큰애보다 크면 
            if deq[-1] > deq[point1]:
                point1 = len(deq)-1
            # 덱이 물건 사용가능 최대 개수보다 길어지면 늙은애하나 없애기
            if len(deq) > K:
                point2 += 1
                if point2 > point1:
                    point1 += 1
            
                
        
print(cache[-1])