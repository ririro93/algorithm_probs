from sys import stdin
from collections import deque

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N, K = map(int, input().split())
ls = [len(input().rstrip()) for _ in range(N)]

# init
deq = deque(ls[:K])
dic = {}

# function 
def checkdeq(deq):
    checked = []
    result = 0
    for ele in deq:
        # fill dictionary
        if ele in dic:
            dic[ele] += 1
        else:
            dic[ele] = 1
        # get initial cnt
        if ele in checked:
            continue
        checked.append(ele)
        n = list(deq).count(ele)
        result += int(n * (n-1) / 2)  
    return result

# exe
## check inside deque
cnt = checkdeq(deq)

## check students
for num in ls[K:]:
    if num in dic:
        cnt += dic[num]
        dic[num] += 1
    else:
        dic[num] = 1
    popped = deq.popleft()
    dic[popped] -= 1
    deq.append(num)
print(cnt)  