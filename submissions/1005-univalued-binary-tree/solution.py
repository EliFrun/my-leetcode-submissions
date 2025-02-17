# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def solve(v, node):
            if not node:
                return True
            return node.val == v and solve(v, node.left) and solve(v, node.right)
        
        return solve(root.val, root)
        
