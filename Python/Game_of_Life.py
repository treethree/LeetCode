# O(mn) time O(1) extra space
class Solution:
    def update(self, board, m, n, i, j):
        live = 0
        for p in range(max(i - 1, 0), min(i + 2, m)):
            for q in range(max(j - 1, 0), min(j + 2, n)):
                live += board[p][q] & 1
        if live == 3 or live == board[i][j] + 3:
            board[i][j] += 2
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                self.update(board, m, n, i, j)
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

# the key point is to understand that the change to a cell is only decided by its nearby 8 cell in the original grid.
#
# we should not use the updated cell to compute to change decision for other cell,therefore, the brute force way is to store the result in a new grid,then assign result back
#
# But usually it requires use O(1) space, so the problem becomes: How can we store store the middle result without use extra space.
#
# the solution is to store the result in the origin grid as different number by some rule, so when we compute decision for other cell, we can know the original value of those nearby cell which has already been updated based on the rule
#
# for example, we can do like this
# 
# living cells nearby | change | new value
#
# <2        1->0     2
# 2,3       1->1     1
# >3        1->0     2
# 3         0->1     3
# so when we count living cells nearby, we need to count those value equals to 1 and 2

class Solution2:
    def gameOfLife(self, board):
        if not board or len(board[0]) == 0:
            return
        m, n = len(board), len(board[0])
        for i, row in enumerate(board):
            for j, ele in enumerate(row):
                count = 0
                for a in range(max(0, i - 1), min(i + 2, m)):
                    for b in range(max(0, j - 1), min(j + 2, n)):
                        if (a, b) != (i, j) and 1 <= board[a][b] <= 2:
                            count += 1
                if board[i][j] == 0:
                    if count == 3:
                        board[i][j] = 3
                else:
                    if count < 2 or count > 3:
                        board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1
