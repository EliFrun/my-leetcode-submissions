# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        best = 0
        def solve(node, above_sum):
            if not node:
                return
            above_sum += node.val
            nonlocal best
            best = max(best, (above_sum + solve2(node.left)) * solve2(node.right), (above_sum + solve2(node.right)) * solve2(node.left))
            solve(node.left, above_sum + solve2(node.right))
            solve(node.right, above_sum + solve2(node.left))

        @cache
        def solve2(node):
            if not node:
                return 0
            return node.val + solve2(node.left) + solve2(node.right)

        solve(root, 0)

        return best % 1_000_000_007
        
