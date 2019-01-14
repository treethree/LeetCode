# Any other number not it the list should be considered as invalid.
# So if you XOR them altogether, you will get a mask value, which is:
#
# 1010101010101010101010101010101 (1431655765)
# Any number which is power of 4, it should be power of 2, I use num &(num-1) == 0 to make sure of that.
# Obviously 0 is not power of 4, I have to check it.
# and finally I need to check that if the number 'AND' the mask value is itself, to make sure it's in the list above.
#
# here comes the final code:
#
# return num != 0 and num &(num-1) == 0 and num & 1431655765== num

class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num != 0 and num &(num-1) == 0 and num & 1431655765== num
