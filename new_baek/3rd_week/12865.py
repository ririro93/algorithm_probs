from sys import stdin

stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N, K = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(N)]

# init -> highest : less weight could value more [index, val]
cache_val = [0] + [-1] * K
cache_what = [[] for _ in range(K+1)] # check what's in kth weight
highest = [0, 0]
max_val = sum([v for _, v in infos])

# function
def solve(highest, max_val):
    for t in range(1, K+1):
        # loop through all weights and store highest value to tmp
        cache_what[t] = cache_what[highest[0]][:]
        cache_val[t] = highest[1]
        for i, [w, val] in enumerate(infos):
            if t - w >= 0:
                tmp_val = cache_val[t - w] + val
                if tmp_val > highest[1] and i not in cache_what[t - w]:
                    # print('tmp_val:', tmp_val, ' w:', w)
                    cache_what[t] = cache_what[t - w][:]
                    cache_what[t].append(i)
                    cache_val[t] = tmp_val
                    highest = [t, tmp_val]
                    if highest[1] == max_val:
                        # print(t)
                        # print(*cache_what, sep='\n')
                        # print(cache_val)
                        return highest[1]
        # print(*cache_what, sep='\n')
        # print(cache_val)
    return highest[1]

# exe
print(solve(highest, max_val))
    
            
            