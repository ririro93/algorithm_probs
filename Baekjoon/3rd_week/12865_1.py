from sys import stdin
from heapq import heappush, heappop

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N, K = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(N)]

# function
def solve(K):
    checked = [-0]
    cache = [0] * (K+1)
    max_val = sum([val for _, val in infos])
    for info in infos:
        checklist = []
        nchecked = []
        l = len(checked)
        for _ in range(l):
            checklist.append(heappop(checked))
        for ele in checklist:
            tmp_val = cache[-ele] + info[1]
            tmp_weight = -ele + info[0]
            if tmp_weight <= K and tmp_val > cache[tmp_weight]:
                if tmp_val == max_val:
                    return tmp_val
                cache[tmp_weight] = tmp_val
                nchecked.append(tmp_weight)
        for nele in nchecked:
            heappush(checklist, -nele)
        checked = checklist[:]
        # print('\ncache: ', cache[:K+1])
        # print('checked: ', checked)
    return max(cache)

# exe
print(solve(K))