# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        if targetSum - root.val == 0 and not root.left and not root.right:
            return [[root.val]]
        
        return (
            [] +
            [[root.val] + x for x in self.pathSum(root.left, targetSum  - root.val)] +
            [[root.val] + x for x in self.pathSum(root.right, targetSum  - root.val)]
        )
