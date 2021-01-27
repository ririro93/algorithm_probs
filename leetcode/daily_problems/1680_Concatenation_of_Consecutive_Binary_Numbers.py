class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = 1
        x = int(log(n, 2))

        # f(n) = (2**x) * f(n-1) + n
        for i in range(2, n+1):
            x = int(log(i, 2)) + 1
            result = (2**x) * result + i
            result %= int(1e9 + 7)
        
        return result