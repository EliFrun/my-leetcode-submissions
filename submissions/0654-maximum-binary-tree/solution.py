# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def solve(lis):
            if not lis:
                return None
            return TreeNode(
                max(lis),
                solve(lis[:lis.index(max(lis))]),
                solve(lis[lis.index(max(lis)) + 1:])
            )

        return solve(nums)
        
