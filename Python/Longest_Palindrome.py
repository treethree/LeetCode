class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        ans = 0
        for i in s:
            dic[i] = dic.get(i,0) + 1
        for val in dic.values():
            ans += val // 2 * 2
            if ans % 2 == 0 and val % 2 == 1:
                ans += 1
        return ans


            
