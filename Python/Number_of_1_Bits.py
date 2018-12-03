# Complexity Analysis
#
# The run time depends on the number of bits in n. Because n in this piece of code is a 32-bit integer, the time complexity is O(1).
#
# The space complexity is O(1), since no additional space is allocated.
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count , mask = 0, 1
        for i in range(32):
            if n & mask != 0:
                count += 1
            mask <<= 1
        return count
