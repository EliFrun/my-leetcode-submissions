# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ret = None

        def dfs(curr):
            nonlocal ret
            if not curr:
                return False
            res = False
            if curr == p:
                res = True
            if curr == q:
                res = True
            
            l = dfs(curr.left)
            r = dfs(curr.right)
            if (res and (l or r)) or (l and r):
                if not ret:
                    ret = curr
            return l or r or res
        dfs(root)

        return ret
            
        

