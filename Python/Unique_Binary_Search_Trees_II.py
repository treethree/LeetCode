# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n: return []
        return self.dfs(1,n)
    def dfs(self, start, end):
        if start > end: return [None]
        res = []
        for rootVal in range(start, end+1):
            leftTree = self.dfs(start,rootVal-1)
            rightTree = self.dfs(rootVal+1,end)
            for i in leftTree:
                for j in rightTree:
                    root = TreeNode(rootVal)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res
