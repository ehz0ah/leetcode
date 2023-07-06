# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root,depth):
            if not root:
                return depth
            if not root.left and not root.right:
                return 1
            if not root.left:
                return dfs(root.right,depth) + 1
            if not root.right:
                return dfs(root.left,depth) + 1
            return min(dfs(root.left,depth), dfs(root.right,depth)) + 1
        return dfs(root,0)