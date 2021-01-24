"""
:type matrix: List[List[int]]
:type k: int
:rtype: int
"""
class Solution(object):
    def kthLargestValue(self, matrix, k):
        # init
        m = len(matrix)
        n = len(matrix[0])
        G = [[0 for _ in range(n)] for _ in range(m)]
        G[0][0] = matrix[0][0]
        result = []
        
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if i == 0 and j != 0:
                    G[i][j] = G[i][j-1] ^ matrix[i][j]
                elif i != 0 and j == 0:
                    G[i][j] = G[i-1][j] ^ matrix[i][j]
                elif i != 0 and j != 0:
                    G[i][j] = G[i-1][j] ^ G[i][j-1] ^ G[i-1][j-1] ^ matrix[i][j]
        
        for i, row in enumerate(G):
            for j, col in enumerate(row):      
                result.append(G[i][j])
        result.sort()
        return result[-k]
                