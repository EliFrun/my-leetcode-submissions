# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        lca = None
        def solve(curr):
            nonlocal lca
            if not curr:
                return 0
            ret = 0
            if curr == p:
                ret += 1
            if curr == q:
                ret += 1
            
            ret += solve(curr.left) + solve(curr.right)
            if ret == 2 and not lca:
                lca = curr
            return ret

        solve(root)
        return lca
            
        
