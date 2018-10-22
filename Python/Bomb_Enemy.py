# Description
# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
#
# You can only put the bomb at an empty cell.
#
# Have you met this question in a real interview?
# Example
# Given a grid:
#
# 0 E 0 0
# E 0 W E
# 0 E 0 0
# return 3. (Placing a bomb at (1,1) kills 3 enemies)

# 这种解法比较省空间，写法也比较简洁，需要一个rowCnt变量，用来记录到下一个墙之前的敌人个数。
# 还需要一个数组colCnt，其中colCnt[j]表示第j列到下一个墙之前的敌人个数。算法思路是遍历整个数组grid，
# 对于一个位置grid[i][j]，对于水平方向，如果当前位置是开头一个或者前面一个是墙壁，我们开始从当前位置往后遍历，
# 遍历到末尾或者墙的位置停止，计算敌人个数。对于竖直方向也是同样，如果当前位置是开头一个或者上面一个是墙壁，
# 我们开始从当前位置向下遍历，遍历到末尾或者墙的位置停止，计算敌人个数。可能会有人有疑问，为啥rowCnt就可以用一个变量，
# 而colCnt就需要用一个数组呢，为啥colCnt不能也用一个变量呢？原因是由我们的遍历顺序决定的，我们是逐行遍历的，
# 在每行的开头就统计了该行的敌人总数，所以在该行遍历没必要用数组，但是每次移动时就会换到不同的列，
# 我们总不能没每个列就重新统计一遍吧，所以就在第一行时一起统计了存到数组中供后来使用。有了水平方向和竖直方向敌人的个数，
# 那么如果当前位置是0，表示可以放炸弹，我们更新结果res即可.

class Solution:
    def maxKilledEnemies(self, grid):
        # write your code here
        if not grid or not grid[0]: return 0
        res = 0
        row_cnt = 0
        col_cnt = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not j or grid[i][j-1] == 'W':
                    row_cnt = 0
                    k = j
                    while k < len(grid[0]) and grid[i][k] != 'W':
                        if grid[i][k] == 'E':
                            row_cnt += 1
                        k += 1
                if not i or grid[i-1][j] == 'W':
                    col_cnt[j] = 0
                    k = i
                    while k < len(grid) and grid[k][j] != 'W':
                        if grid[k][j] == 'E':
                            col_cnt[j] += 1
                        k += 1
                if grid[i][j] == '0':
                    res = max(res, row_cnt + col_cnt[j])
        return res
