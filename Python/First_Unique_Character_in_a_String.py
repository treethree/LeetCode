class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1

        for i, char in enumerate(s):
            if dic[char] and dic[char] == 1:
                return i
        return -1
