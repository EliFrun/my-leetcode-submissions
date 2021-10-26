# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum_path = -1_000_000_000
        def dfs(node):
            nonlocal maximum_path
            if not node:
                return 0
            
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            maximum_path = max(maximum_path, node.val + left + right)
            return node.val + max(left, right)
        
        dfs(root)
        return maximum_path
            
    
        
        
