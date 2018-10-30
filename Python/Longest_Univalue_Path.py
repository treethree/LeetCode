# Algorithm
#
# Let arrow_length(node) be the length of the longest arrow that extends from the node. That will be 1 + arrow_length(node.left) if node.left exists and has the same value as node. Similarly for the node.right case.
#
# While we are computing arrow lengths, each candidate answer will be the sum of the arrows in both directions from that node. We record these candidate answers and return the best one.

#Hence at the end of each recursive loop, return the longest length using that node as the root so that the node's parent can potentially use it in its longest path computation.

class Solution(object):
    def longestUnivaluePath(self, root):
        self.ans = 0

        def arrow_length(node):
            if not node: return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans

#Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the tree. We process every node once.
#
# Space Complexity: O(H), where H is the height of the tree. Our recursive call stack could be up to H layers deep.
