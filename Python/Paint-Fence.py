# Description
# There is a fence with n posts, each post can be painted with one of the k colors.
# You have to paint all the posts such that no more than two adjacent fence posts have the same color.
# Return the total number of ways you can paint the fence.
# n and k are non-negative integers.
# Example
# Given n=3, k=2 return 6
#       post 1,   post 2, post 3
# way1    0         0       1
# way2    0         1       0
# way3    0         1       1
# way4    1         0       0
# way5    1         0       1
# way6    1         1       0

# Time:  O(n)
# Space: O(1)
class Solution():
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return k
        dp = [0] * 3
        dp[0] = k
        dp[1] = (k - 1) * dp[0] + k
        for i in range(2, n):
            dp[i % 3] = (k - 1) * (dp[(i - 1) % 3] + dp[(i - 2) % 3])
        return dp[(n - 1) % 3]

# Time:  O(n)
# Space: O(n)
# DP solution.
#用DP，DP[i]表示第i个柱子最多的选择数。在计算DP[i]时，考虑两种情况：
#1.和第i－1柱子不同颜色，则可以有(k-1) * DP[i-1]个选择
#2.和第i－1柱子相同颜色，此时要求i－1柱子和i－2柱子不同颜色（即第一种情况，只是换成了第i－1根柱子和第i－2根柱子不同颜色），所以有(k-1) * DP[i-2]个选择
#3.因此总选择数为(k-1) * (DP[i-1] + DP[i-2])
#因为只和前两个柱子相关，所以可以用滚动数组来优化空间

class Solution2():
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return k
        dp = [0] * n
        dp[0] = k
        dp[1] = (k - 1) * dp[0] + k
        for i in range(2, n):
            dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2])
        return dp[n - 1]
