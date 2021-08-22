# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if not root:
            return
        lis = self.preorder(root)
        
        head = lis[0]
        previous = lis[0]
        for l in lis[1:]:
            previous.left = None
            previous.right = l
            previous = l
        
        
    def preorder(self, root):
        if not root:
            return []
        
        ret = [root]
        
        if root.left:
            ret.extend(self.preorder(root.left))
        if root.right:
            ret.extend(self.preorder(root.right))
            
            
        return ret
