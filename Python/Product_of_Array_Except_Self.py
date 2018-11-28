# The idea is that for each element of the array, you would want to multiply all the elements to the left and right.
#So in the first for loop you are cumulatively multiplying all the previous elements to each other in each iteration,
#essentially multiplying all the elements to the left of the element. In the second for loop, you will be doing the same now except now in reverse as you will be multiplying all the elements to the right.
#
# [1, 2, 3, 4] <---- input
# [1]
# [1, 1]
# [1, 1, 2]
# [1, 1, 2, 6]
# [1, 1, 2, 6] *note that the last element of the array is already its answer because it is the product of all the elements to the left of it
# [1, 1, 8, 6]
# [1, 12, 8, 6]
# [24, 12, 8, 6]

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output
