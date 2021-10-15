# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = [-1000000000]
        
        def dfs(node, a):
            if not node:
                return 0
            # since any path, we can exclude a path if its below 0
            left = max(dfs(node.left, a), 0)
            right = max(dfs(node.right, a), 0)
            a[0] = max(a[0], left + right + node.val)
            return max(left + node.val, right + node.val)
        
        dfs(root, max_path)
        return max_path[0]
    
        
        
