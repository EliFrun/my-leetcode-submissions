# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = self.inorder(root)
        for v in s:
            if k - v in s.difference(set([v])):
                return True
        return False
        
    def inorder(self, root):
        if not root:
            return set()
        
        return self.inorder(root.left).union(set([root.val])).union(self.inorder(root.right))
        
