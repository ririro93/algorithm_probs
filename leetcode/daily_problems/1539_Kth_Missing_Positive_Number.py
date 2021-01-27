class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        last = arr[-1]
        cnt = 0
        for i in range(1, last+k+1):
            if i not in arr:
                cnt += 1
            if cnt == k:
                return i