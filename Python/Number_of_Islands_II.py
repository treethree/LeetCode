# A 2d grid map of m rows and n columns is initially filled with water. We may
# perform an addLand operation which turns the water at position (row, col) into a land.
# Given a list of positions to operate, count the number of islands after each
# addLand operation. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of the grid
# are all surrounded by water.
# Example:
# Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]. Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).
# 0 0 0
# 0 0 0
# 0 0 0
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
# We return the result as an array: [1, 1, 2, 3].

#Union Find Algorithms reference https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf
#Time: O(k*lgmn)
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        # find the root of a point
        def find(x, uf):
            while x != uf[x]:
                #Path compression
                uf[x] = uf[uf[x]]
                x = uf[x]
            return x

        island_groups, res, uf, idx = set(), [], {}, 1
        for i, j in positions:
            uf[(i, j)] = uf[idx] = idx
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                # when neighbor == 1, we make cur_point as the root
                if (x, y) in uf:
                    root = find(uf[(x, y)], uf)
                    island_groups.discard(root)
                    uf[root] = idx
            island_groups.add(idx)
            idx += 1
            res.append(len(island_groups))
        return res
