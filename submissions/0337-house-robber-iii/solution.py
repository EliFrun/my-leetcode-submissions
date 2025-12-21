# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def solve(node, prev_robbed):
            if not node:
                return 0

            ret = solve(node.left, False) + solve(node.right, False)
            if not prev_robbed:
                ret = max(ret, node.val + solve(node.left, True) + solve(node.right, True))
            return ret

        return solve(root, False)
        
