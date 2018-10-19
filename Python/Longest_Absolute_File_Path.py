class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxLen, path = 0, []
        for i in input.split("\n"):
            path[i.count('\t'):] = [len(i.strip('\t'))]
            maxLen = max(maxLen, sum(path) + len(path)-1 if '.' in i else 0)
        return maxLen
