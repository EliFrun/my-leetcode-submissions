# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        def solve(node, val):
            if not node:
                return 0
            val = (val << 1) + node.val
            if not node.left and not node.right:
                return val
            return solve(node.left, val) + solve(node.right, val)

        return solve(root, 0)
        
