# Description
# A mirror number is a number that looks the same when rotated 180 degrees (looked at upside down).
#
# Write a function to determine if a number is mirror. The number is represented as a string.
#
# Example
# For example, the numbers "69", "88", and "818" are all mirror numbers.
# Given num = "69" return true
# Given num = "68" return false

class Solution:
    def isStrobogrammatic(self, num):
        # write your code here
        d = {'6':'9','9':'6','1':'1','0':'0','8':'8'}
        p1,p2 = 0,len(num)-1
        while p1 <= p2:
            if num[p1] not in d or num[p2] not in d:
                return False
            if d[num[p1]] != num[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True
