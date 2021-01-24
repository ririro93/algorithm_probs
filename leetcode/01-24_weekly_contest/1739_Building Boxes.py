class Solution:
    def minimumBoxes(self, n: int) -> int:
        if n <= 3:
            return n
        # sums contains max blocks for each height
        cnt = 0
        i = 1
        sums = [] 
        diffs = [1]
        while cnt <= 1e9:
            c = int(i * (i + 1) / 2)
            cnt += c
            sums.append(cnt)
            diffs.append(c+1)
            i += 1
        print(sums)
        # former = max num of blocks for current height
        for h in range(len(sums)):
            if sums[h] > n:
                former = sums[h-1] - sums[h-2]
                diff = n - sums[h-1]
                if diff == 0:
                    return former
                for j in range(len(diffs)):
                    if diffs[j] > diff:
                        print(diffs[j], diff)
                        print(j)
                        return former + j