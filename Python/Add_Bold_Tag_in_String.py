# Description
# Given a string s and a list of strings dict, you need to add a closed pair of bold tag and to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
#
# The given dict won't contain duplicates, and its length won't exceed 100.
# All the strings in input have length in range [1, 1000].
#
# Have you met this question in a real interview?
# Example
# Input:
# s = "abcxyz123"
# dict = ["abc","123"]
# Output:
# "<b>abc</b>xyz<b>123</b>"
# Input:
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# Output:
# "<b>aaabbc</b>c"
 # Approach #3 Using Boolean(Marking) Array
 # Time complexity : O(l*s*x). Three nested loops are there to fill boldbold array.
 # Space complexity : O(s). resres and boldbold size grows upto O(s).

class Solution:
    def addBoldTag(self, s, dict):
        # write your code here
        bold = [False] * len(s)
        for i in dict:
            for j in range(len(s) - len(i)+1):
                if s[j:j+len(i)] == i:
                    for k in range(j , len(i) + j):
                        bold[k] = True
        res, i = [] , 0
        while i < len(s):
            if bold[i]:
                res.append("<b>")
                while i < len(s) and bold[i]:
                    res.append(s[i])
                    i += 1
                res.append("</b>")
            else:
                res.append(s[i])
                i += 1
        return ''.join(res)
