class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1: return False
        if n == 1: return True

        while n > 1:
            if n % 3 != 0:
                return False
            n /= 3

        return True

class Solution2:
    return n > 0 and 3 ** round(math.log(n, 3)) == n
