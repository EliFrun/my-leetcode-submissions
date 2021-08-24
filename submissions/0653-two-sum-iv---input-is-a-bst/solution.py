# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        for i in self.toList(root):
            if k - i == i:
                continue
            if self.inTree(root, k - i):
                return True
            
        return False
        
        
    def toList(self, root):
        if not root:
            return []
        
        return self.toList(root.left) + [root.val] + self.toList(root.right)
        
        
    def inTree(self, root, k):
        if not root:
            return False
        
        if root.val == k:
            return True
        
        if root.val < k:
            return self.inTree(root.right, k)
        
        if root.val > k:
            return self.inTree(root.left, k)
