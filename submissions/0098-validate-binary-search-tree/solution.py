# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lis = self.inorder(root)

        for i in range(len(lis) - 1):
            if lis[i] >= lis[i + 1]:
                return False
            
        return True
        
        
    def inorder(self, root):
        if not root:
            return []
        ret = []
        if root.left:
            ret.extend(self.inorder(root.left))
            
        ret.append(root.val)
        
        
        if root.right:
            ret.extend(self.inorder(root.right))
            
        return ret
        
    
