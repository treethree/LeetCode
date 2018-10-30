# Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
#
# Example
# Given nums = [-2,0,1,3], target = 2, return 2.
#
# Explanation:
# Because there are two triplets which sums are less than 2:
# [-2, 0, 1]
# [-2, 0, 3]
# Challenge
# Could you solve it in O(n2) runtime?

#题目中的Follow up让我们在O(n^2)的时间复杂度内实现，那么我们借鉴之前那两道题3Sum Closest和3Sum中的方法，
#采用双指针来做，这里面有个trick就是当判断三个数之和小于目标值时，此时结果应该加上right-left，
#以为数组排序了以后，如果加上num[right]小于目标值的话，那么加上一个更小的数必定也会小于目标值，然后我们将左指针右移一位，否则我们将右指针左移一位
# Two Pointers:
class Solution:
    def threeSumSmaller(self, nums, target):
        # Write your code here
        def twoSumSmaller(nums,start,target):
            res = 0
            left = start
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < target:
                    res += right - left
                    left += 1
                else:
                    right -= 1
            return res

        nums.sort()
        res = 0
        for i in range(len(nums) - 2):
            res += twoSumSmaller(nums, i+1, target - nums[i])
        return res
