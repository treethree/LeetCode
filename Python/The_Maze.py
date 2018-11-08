# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
#
# Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.
#
# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.
#
# Example 1
#
# Input 1: a maze represented by a 2D array
#
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
#
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (4, 4)
#
# Output: true
# Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
#
# Example 2
#
# Input 1: a maze represented by a 2D array
#
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
#
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (3, 2)
#
# Output: false
# Explanation: There is no way for the ball to stop at the destination.
#
# Note:
# There is only one ball and one destination in the maze.
# Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
# The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
# The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

# BFS solutuon:
class Solution():
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        queue = [start]
        m = len(maze)
        n = len(maze[0])
        dir = [(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            i, j = queue.pop(0)
            # record
            maze[i][j] = -1
            if i == destination[0] and j == destination[1]:
                return True
            for x, y in dir:
                row = x + i
                col = y + j
                # move until the wall
                while 0<= row < m and 0<= col < n and maze[row][col] != 1:
                    row += x
                    col += y
                # move back a step
                row -= x
                col -= y
                if maze[row][col] == 0 and [row,col] not in queue:
                    queue.append([row, col])
        return False

# DFS Solution:
class Solution2():
    def hasPath(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        res = self.dfs(maze, start[0], start[1], destination, visited)
        return res

    def dfs(self, maze, i, j, dest, visited):
        m, n, res = len(maze), len(maze[0]), False
        if i == dest[0] and j == dest[1]:
            visited[i][j] = True
            return True
        visited[i][j] = True
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        for _dir in dirs:
            x, y = i, j
            while x >=0 and x < m and y >=0 and y < n and maze[x][y] == 0:
                x += _dir[0]
                y += _dir[1]
            x -= _dir[0]
            y -= _dir[1]
            if not visited[x][y]:
                res |= self.dfs(maze, x, y, dest, visited)
        return res
