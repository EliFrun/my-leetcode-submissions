# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        
        root_index = 0
        for i in enumerate(inorder):
            if i[1] == preorder[0]:
                root_index = i[0]
                
        left = inorder[:root_index]
        right = inorder[root_index + 1:]
                
        if left:
            root.left = self.buildTree(preorder[1: 1 + len(left)], left)
        
        if right:
            root.right = self.buildTree(preorder[len(left) + 1:], right)
            
        return root
            
            
            
            
        
