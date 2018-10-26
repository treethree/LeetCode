#Approach #1: Group by Category [Accepted]
# Intuition and Algorithm
#
# We ask what feature makes two coordinates (r1, c1) and (r2, c2) belong to the same diagonal?
#
# It turns out two coordinates are on the same diagonal if and only if r1 - c1 == r2 - c2.
#
# This leads to the following idea: remember the value of that diagonal as groups[r-c]. If we see a mismatch, the matrix is not Toeplitz; otherwise it is.
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True
# Complexity Analysis
#
# Time Complexity: O(M*N). (Recall in the problem statement that M, N are the number of rows and columns in matrix.)
#
# Space Complexity: O(M*N)

#Approach #2: Compare With Top-Left Neighbor [Accepted]
class Solution2(object):
    def isToeplitzMatrix(self, matrix):
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))

class Solution2:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if i>0 and j>0 and matrix[i-1][j-1] != val:
                    return False
        return True
#Time Complexity: O(M*N)
#Space Complexity: O(1).
