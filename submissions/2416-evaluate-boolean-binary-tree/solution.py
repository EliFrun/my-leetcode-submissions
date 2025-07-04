# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def solve(node):
            if node.val == 0:
                return False
            if node.val == 1:
                return True
            if node.val == 2:
                return solve(node.left) or solve(node.right)
            if node.val == 3:
                return solve(node.left) and solve(node.right)

        return solve(root)
        
