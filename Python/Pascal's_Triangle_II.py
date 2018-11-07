class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        for i in range(1,rowIndex+2):
            # there are i elements
            result.append(1)
            for j in range(i-2,0,-1):
                result[j] += result[j-1]
        return result

class Solution2:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row
