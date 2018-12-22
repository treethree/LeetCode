#Time Complexity O(N^2)
#Space Complexity O(N^2)
#dp[i][j]: 表示正方形右下角可延伸的最大边长
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m , n = len(matrix), len(matrix[0])
        dp = [[ 0 if matrix[i][j] == '0' else 1 for j in range(0, n)] for i in range(0, m)]

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = 0

        res = max(max(row) for row in dp)
        return res ** 2
