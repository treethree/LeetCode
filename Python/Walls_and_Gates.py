# You are given a m x n 2D grid initialized with these three possible values.
#
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
#
# Example
# Given the 2D grid:
#
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# return the result:
#
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4
# BFS:
class Solution:
    def wallsAndGates(self, rooms):
        # write your code here
        m = len(rooms)
        n = len(rooms[0])
        INF = 2147483647
        def bfs(i,j,count):
            dir = [(0,-1),(0,1),(1,0),(-1,0)]
            for x , y in dir:
                x += i
                y += j
                if 0 <= x < m and 0 <= y < n and rooms[x][y] > count:
                    rooms[x][y] = count
                    bfs(x,y,count + 1)

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    bfs(i,j,1)
