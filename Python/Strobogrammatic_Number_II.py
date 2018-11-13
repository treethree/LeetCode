# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Find all strobogrammatic numbers that are of length = n.
#
# Example
# Given n = 2, return ["11","69","88","96"].

class Solution:
    def findStrobogrammatic(self, n):
        # write your code here
        result = self.numdef(n, n)
        return result

    def numdef(self,n, length):

        if n == 0: return [""]
        if n == 1: return ["1", "0", "8"]

        middles = self.numdef(n - 2, length)
        result = []

        for middle in middles:
            if n != length:
                result.append("0" + middle + "0")

            result.append("8" + middle + "8")
            result.append("1" + middle + "1")
            result.append("9" + middle + "6")
            result.append("6" + middle + "9")
        return result
