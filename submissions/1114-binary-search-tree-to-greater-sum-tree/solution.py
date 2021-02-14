# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        Solution.total = 0
        self.convert(root)
        return root
        
        
    total = 0
    def convert(self, root: TreeNode):
        if root.right is not None:
            tmp = self.convert(root.right)
            
        Solution.total += root.val
        root.val = Solution.total

        if root.left is not None:
            self.convert(root.left)
            
                

            
