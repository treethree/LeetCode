# Bottom up, O(n) space
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        res = [0 for i in range(n)]
        res[0], res[1] = 1, 2
        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[-1]


# Top down + memorization (list)
class Solution2:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        dic = [-1 for i in range(n)]
        dic[0], dic[1] = 1, 2
        return self.helper(n-1, dic)

    def helper(self, n, dic):
        if dic[n] < 0:
            dic[n] = self.helper(n-1, dic)+self.helper(n-2, dic)
        return dic[n]
