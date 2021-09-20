# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(root):
            if not root:
                return []
            
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        a = inorder(root)
        ret = 100000
        
        for i in range(1, len(a)):
            ret = min(ret, abs(a[i - 1] - a[i]))    
            
        return ret
            
