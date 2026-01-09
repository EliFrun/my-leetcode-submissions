# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ret = None
        deepest = 0
        def dfs(node, depth):
            nonlocal ret
            nonlocal deepest
            if not node:
                return 0

            l = dfs(node.left, depth + 1)
            r = dfs(node.right, depth + 1)
            if l == r and depth + l >= deepest:
                deepest = depth + l
                ret = node

            return 1 + max(l, r)
                

        dfs(root, 0)
        return ret
        
