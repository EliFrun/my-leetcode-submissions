# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def solve(node):
            if not node:
                return None
            if val < node.val:
                return solve(node.left)
            if val > node.val:
                return solve(node.right)
            return node
        return solve(root)
        
