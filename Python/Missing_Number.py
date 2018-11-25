class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res1 = 0
        l = len(nums)
        for i, num in enumerate(nums):
            res1 ^= num ^ i
        res = l ^ res1
        return res
