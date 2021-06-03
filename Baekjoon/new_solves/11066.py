from sys import stdin

# stdin = open('inputs.txt', 'r')
input = stdin.readline

################ 파일 합치기
# dp[i][j] 가 i번 파일부터 j번 파일까지 더할 때의 최소비용을 의미하는 2차원 dp 배열을 만들고 채워나가기
# cf). https://data-make.tistory.com/402

T = int(input())
for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))

    # init
    dp = [[0] * K for _ in range(K)]    
    step = 1

    while step < K:
        for i in range(K-step):
            costs = []
            for k in range(step):
                costs.append(dp[i][i+k] + dp[i+k+1][i+step])
            dp[i][i+step] = sum(files[i:i+step+1]) + min(costs)
        step += 1

    print(dp[0][-1])
    