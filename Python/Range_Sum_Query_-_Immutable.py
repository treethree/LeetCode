class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dc = {-1:0}
        for i,v in enumerate(nums):
            self.dc[i] = self.dc[i-1] + v

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dc[j]-self.dc[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
