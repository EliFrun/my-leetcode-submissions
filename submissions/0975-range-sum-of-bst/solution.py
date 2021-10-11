# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inorder(n):
            if not n:
                return []
            return inorder(n.left) + [n.val] + inorder(n.right)
        
        return sum(x for x in inorder(root) if low <= x <= high)
