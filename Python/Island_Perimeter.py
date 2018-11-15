class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])
        p = 0
        for m in range(M):
            for n in range(N):
                if grid[m][n] == 1:
                    p = p+4
                    if m != 0 and grid[m-1][n] == 1:
                        p = p-1
                    if m != M-1 and grid[m+1][n] == 1:
                        p = p-1
                    if n != 0 and grid[m][n-1] == 1:
                        p = p-1
                    if n != N-1 and grid[m][n+1] == 1:
                        p = p-1
        return p

class Solution2:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        def helper(i,j):
            count = 0
            adjacent = [(i-1,j), (i+1,j),(i,j-1),(i,j+1)]
            for i, j in adjacent:
                if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == 0:
                    count += 1
            return count
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += helper(i,j)
        return res
