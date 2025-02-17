# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solve(node, p, q):
            if p <= node.val and q >= node.val:
                return node
            
            if q < node.val:
                return solve(node.left, p, q)
            return solve(node.right, p, q)


        return solve(root, min(p.val,q.val), max(p.val,q.val))
        
