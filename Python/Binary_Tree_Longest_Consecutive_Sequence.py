# Given a binary tree, find the length of the longest consecutive sequence path.
#
# The path refers to any sequence of nodes from some starting node to any node in
# the tree along the parent-child connections. The longest consecutive path need to
# be from parent to child (cannot be the reverse).
#
# Example
# For example,
#
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
# Longest consecutive sequence path is 3-4-5, so return 3.
#
#    2
#     \
#      3
#     /
#    2
#   /
#  1
# Longest consecutive sequence path is 2-3,not3-2-1, so return 2.


class Solution:
    def longestConsecutive(self, root):
        # write your code here
        if not root:
            return 0
        self.res = 0
        self.helper(root,1)
        return self.res

    def helper(self,root,curlen):
        self.res = curlen if curlen > self.res else self.res
        if root.left:
            if root.left.val == root.val + 1:
                self.helper(root.left, curlen + 1)
            else:
                self.helper(root.left,1)
        if root.right:
            if root.right.val == root.val + 1:
                self.helper(root.right, curlen + 1)
            else:
                self.helper(root.right,1)


class Solution2:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code here
        self.max_len = 0
        def helper(root):
            if not root:
                return 0
            left_len = helper(root.left)
            right_len = helper(root.right)
            cur_len = 1
            if root.left and root.left.val == root.val + 1:
                cur_len = max(cur_len, left_len + 1)
            if root.right and root.right.val == root.val + 1:
                cur_len = max(cur_len, right_len + 1)

            self.max_len = max(self.max_len, cur_len, left_len, right_len)

            return cur_len

        helper(root)
        return self.max_len
