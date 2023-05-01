# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def issame(p,q):
            if p == None and q == None:
                return True
            if p == None or q == None:
                return False
            return p.val == q.val and issame(p.left,q.left) and issame(p.right,q.right)
        return issame(p,q)
        

