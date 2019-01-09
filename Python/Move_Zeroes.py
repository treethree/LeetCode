class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0 # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
