# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        def dfs(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            if not node.left:
                return 1+dfs(node.right)
            if not node.right:
                return 1 + dfs(node.left)
            return min(dfs(node.left), dfs(node.right))+1
        return dfs(root)
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        