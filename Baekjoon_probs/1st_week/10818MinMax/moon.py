# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

# import time
# start_time = time.time()

num = int(input())
myArr = sorted(map(int, input().split(' ')))
input_min = myArr[0]
input_max = myArr[-1]
print(input_min, input_max)

# print(time.time() - start_time)


## 다른 사람꺼
import sys
_,*v=map(int,sys.stdin.read().split())
print(min(v),max(v))
