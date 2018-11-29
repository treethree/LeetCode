class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        check = {}
        for i,num in enumerate(nums):
            if num not in check:
                check[target-num]=i
            else:
                return [check[num],i]
