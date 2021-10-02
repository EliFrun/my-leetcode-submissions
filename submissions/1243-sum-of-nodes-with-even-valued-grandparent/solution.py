# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        ret = 0
        if root.val % 2 == 0:
            if root.left:
                if root.left.left:
                    ret += root.left.left.val
                if root.left.right:
                    ret += root.left.right.val
            if root.right:
                if root.right.left:
                    ret += root.right.left.val
                if root.right.right:
                    ret += root.right.right.val
            
        return ret + self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)
