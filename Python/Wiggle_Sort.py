# Description
# Given an unsorted array nums, reorder it in-place such that
#
# nums[0] <= nums[1] >= nums[2] <= nums[3]....
# Please complete the problem in-place.
#
# Have you met this question in a real interview?
# Example
# Given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].

# Approach #1 (Sorting)
class Solution:
    def wiggleSort(self, nums):
        # write your code here
        nums.sort()
        i = 1
        while i < len(nums) - 1:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            i += 2

#Approach #2 (One-pass Swap)
class Solution:
    def wiggleSort(self, nums):
        # write your code here
        for i in range(len(nums)-1):
            if ((i%2 == 0) and nums[i] > nums[i+1] ) or ((i%2 == 1) and
            nums[i] < nums[i+1]):
                nums[i] , nums[i+1] = nums[i+1] , nums[i]
