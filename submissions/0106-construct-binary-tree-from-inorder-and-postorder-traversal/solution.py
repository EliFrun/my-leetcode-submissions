# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(postorder[-1])
        
        root_index = 0
        for i in enumerate(inorder):
            if i[1] == postorder[-1]:
                root_index = i[0]
                
        left = inorder[:root_index]
        right = inorder[root_index + 1:]
        
                
        if left:
            root.left = self.buildTree(left, postorder[:- len(right) - 1])
        
        if right:
            root.right = self.buildTree(right, postorder[- len(right) - 1:-1])
            
        return root
