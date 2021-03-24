from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# function
def checkTmp(s):
    # print(s)
    l = len(s)
    for i in range(2, l):
        if l - (2*i) + 1 < 0:
            return s
        for start in range(l - (2*i) + 1):
            if s[start:start+i] == s[start+i:start+2*i]:
                return False
    
###############################################
# inputs
N = int(input())

# init
arrs = [['1'], ['12'], ['121', '123']]
options = ['1', '2', '3']

# exec
if N < 4:
    print(arrs[N-1][0])
else:
    for i in range(2, N-1):
        results = []
        for num in arrs[i]:
            end = num[-1]
            for new in options:
                if new != end:
                    tmp = checkTmp(num + new)
                    if tmp:
                        results.append(tmp)
        arrs.append(results[:2])
    # for arr in arrs:
    #     print(arr)
    print(arrs[-1][0])
            