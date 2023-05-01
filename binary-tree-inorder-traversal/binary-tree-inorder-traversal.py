# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # current node points to the node you're on now. stack is the list of nodes to be visted and res is the value of the nodes that have ben visited and appended into res
        currentNode = root
        stack, res = [],[]
        while stack or currentNode:
            while currentNode is not None:
                stack.append(currentNode)
                currentNode = currentNode.left
            # when stack.pop() it gives the lest most mode hence it will be in order and then append it into res
            currentNode = stack.pop()
            res.append(currentNode.val)
            currentNode = currentNode.right

        return res