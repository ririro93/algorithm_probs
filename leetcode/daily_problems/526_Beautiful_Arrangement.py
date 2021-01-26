''' -> 첨에 이렇게 했는데 메모리 초과, 시간 초과 다양한 초과가 뜸
from itertools import permutations

class Solution:
    def countArrangement(self, n: int) -> int:
        my_perms = list(permutations(range(1, n+1), n))        
        result = 0
        print(len(my_perms))
        for perm in my_perms:
            for i, ele in enumerate(perm, start=1):
                if i % ele != 0 and ele % i != 0:
                    break
            else:
                result += 1
        return result
'''
'''
# 여기선 dp 느낌으로 해보기
## 좀 해봤는데 안 된다는걸 깨달음
'''
# 그냥 brute force로 하는데 조건 걸어서 애초에 beautiful 성립 안되면 중간에 끊기 -> 알고보니깐 이게 백트래킹?!이네
class Solution:
    def countArrangement(self, n: int) -> int:
        # pick one, use recusion for n-1 elements
        def solve(my_list, cnt):
            # print('solve:', my_list, cnt)
            # one element left and is beautiful
            if len(my_list) == 1:
                if my_list[0] % cnt == 0 or cnt % my_list[0] == 0:
                    self.total += 1
                    return
            
            # more than 1 element
            else:
                for i, ele in enumerate(my_list):
                    curr_list = my_list[:]
                    if ele % cnt == 0 or cnt % ele == 0:
                        curr_list.pop(i)
                        # print('curr_list: ', curr_list)
                        solve(curr_list, cnt+1) 
        
        my_list = list(range(1, n+1))
        self.total = 0
        
        solve(my_list, 1)
        return self.total
        
            
            
