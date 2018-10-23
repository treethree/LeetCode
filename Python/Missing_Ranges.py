# Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
#
# Example
# Given nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99
# return ["2", "4->49", "51->74", "76->99"].

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        nums.append(upper + 1)
        pre = lower - 1
        for i in nums:
            if i == pre + 2:
                res.append(str(i-1))
            elif i > pre + 2:
                res.append(str(pre+1) + '->' + str(i-1))
            pre = i
        return res
