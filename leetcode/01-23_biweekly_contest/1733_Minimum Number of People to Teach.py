''' 고수 코드
class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        toTeach = set()
        for u, v in friendships:
            if len(set(languages[u-1]).intersection(languages[v-1])) == 0:
                toTeach.add(u-1)
                toTeach.add(v-1)
        print(toTeach)
        l = [0] * n
        for i in toTeach:
            for la in languages[i]:
                l[la-1] += 1
        return len(toTeach) - max(l)
'''

# 내 코드 -> 37, 40번째 줄에서 탐색을 해서 time complexity 가 O(N^2*len(friendships))나 됨 
from copy import deepcopy

class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        result = len(languages)
        for lang in range(1, n+1):
            new_lang = deepcopy(languages)
            cnt = 0
            for f in friendships:
                a, b = f
                seta = set(new_lang[a-1])
                setb = set(new_lang[b-1])
                if not seta & setb:
                    if lang not in new_lang[a-1]:
                        new_lang[a-1].append(lang)
                        cnt += 1
                    if lang not in new_lang[b-1]:
                        new_lang[b-1].append(lang)
                        cnt += 1
            result = min(result, cnt)
        return result