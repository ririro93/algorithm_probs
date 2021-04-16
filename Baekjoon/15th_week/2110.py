from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

## 2110. 공유기 설치
"""
- 와이파이 간 최대거리 가정하고 C개 설치할 수 있나 확인
    - 가능하면 최대거리 늘린 값으로 가정하고 확인
    - 불가능하면 최대거리 줄여서 가정하고 확인
    - 초기값: min: 1, max: X[-1] - X[0]
"""
# functions
def divide(mn, mx):
    if mn == mx:
        check(mn)
        return

    mid = (mn+mx) // 2
    flag = check(mid)
    if flag:
        divide(mid+1, mx)
    else:
        divide(mn, mid-1)

def check(mid):
    # init
    global N, C, result
    curr = X[0]
    cnt = 1

    # exec
    for i in range(1, N):
        if X[i] - curr >= mid:
            curr = X[i]
            cnt += 1
            if cnt == C:
                result = mid 
                return True
    return False

#######################################
# inputs
N, C = map(int, input().split())
X = [int(input()) for _ in range(N)]

# init
X.sort()
result = 10

# exec
divide(mn=1, mx=X[-1]-X[0])
print(result)