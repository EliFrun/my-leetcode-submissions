# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ret = -1_000_000_000
        def dfs(node):
            if not node:
                return 0
            nonlocal ret
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            ret = max(ret, left + right + node.val)
            
            return max(left + node.val, right + node.val)
        
        dfs(root)
        return ret
    
        
        
