# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, n: Optional[TreeNode]) -> str:
        def dfs(root):
            if not root:
                return ""
            if not root.left and not root.right:
                return str(root.val)
            elif not root.right and root.left:
                return str(root.val) + "(" + dfs(root.left) + ")" 
            else:
                return str(root.val) + "(" + dfs(root.left) + ")" + "(" + dfs(root.right) + ")"
        
        return dfs(n)
