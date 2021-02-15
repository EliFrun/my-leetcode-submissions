# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        
        m = max(nums)
        i = nums.index(m)
        return TreeNode(m, self.constructMaximumBinaryTree(nums[0:i]), self.constructMaximumBinaryTree(nums[i + 1:]))
        
