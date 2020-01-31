# 입력은 여러 개의 테스트 케이스로 이루어져 있다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# while True:
    # print(sum(map(int, input().split(' '))))
    # 스페이스 눌르면서 입력을 계속하면 언제 끝날지 어떻게 알지?? 걍 5줄 입력하게 첨부터 설정하면 되나
    # https://www.acmicpc.net/problem/10951

sum1 = sum(map(int, input().split(' ')))
sum2 = sum(map(int, input().split(' ')))
sum3 = sum(map(int, input().split(' ')))
sum4 = sum(map(int, input().split(' ')))
sum5 = sum(map(int, input().split(' ')))
print(sum1)
print(sum2)
print(sum3)
print(sum4)
print(sum5)

# 얘도 아니네