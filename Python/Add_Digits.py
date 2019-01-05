class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            res = 0
            while num > 0:
                res += num % 10
                num //= 10
            num = res
        return num


            
