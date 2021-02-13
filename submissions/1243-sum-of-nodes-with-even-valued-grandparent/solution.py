# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = 0
        if root.val % 2 == 0:
            if root.left is not None:
                if root.left.left is not None:
                    total += root.left.left.val
                if root.left.right is not None:
                    total += root.left.right.val
            if root.right is not None:
                if root.right.left is not None:
                    total += root.right.left.val
                if root.right.right is not None:
                    total += root.right.right.val
                    
        if root.left is not None:
            total += self.sumEvenGrandparent(root.left)
        if root.right is not None:
            total += self.sumEvenGrandparent(root.right)
            
        return total
