from sys import stdin
from collections import deque

# stdin = open('input.txt', 'r')
input = stdin.readline

# functions
def getCombis(start, k):
    # init
    global num_oper, max_num_oper
    
    # exec
    combis.append(checked[:])
    if k == max_num_oper:
        return
    for i in range(start, num_oper):
        checked[i] = True
        getCombis(i+2, k+1)
        checked[i] = False

def calculate(S, combi):
    # init
    cnt = 0
    deq = deque()
    calc = False
    
    # exec (first calc)
    for s in S:
        if s in ['+', '-', '*']:
            deq.append(s)
            if combi[cnt]:
                calc = True
            cnt += 1
        else:
            if calc:
                b = s
                oper = deq.pop()
                a = deq.pop()
                c = eval(a+oper+b)
                deq.append(str(c))
                calc = False
            else:
                deq.append(s)

    # second calc
    while len(deq) > 1:
        a = deq.popleft()
        oper = deq.popleft()
        b = deq.popleft()
        c = eval(a+oper+b)
        deq.appendleft(str(c))
    return int(deq[0])
###########################################    
# inputs
N = int(input())
S = input().rstrip()

# init
num_oper = N // 2
max_num_oper = (num_oper+1) // 2
checked = [False] * num_oper
combis = []
result = -(2**31)

# exec
getCombis(0, 0)

for combi in combis:
    result = max(result, calculate(S, combi))
print(result)
