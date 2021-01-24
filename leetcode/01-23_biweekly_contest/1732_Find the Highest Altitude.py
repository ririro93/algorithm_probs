class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        total = 0
        result = [0]
        for alt in gain:
            total += alt
            result.append(total)
        return max(result)
        