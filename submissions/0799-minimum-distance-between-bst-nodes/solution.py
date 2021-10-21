# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if not node:
                return []
            
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        ret = inorder(root)
        return min(ret[i + 1] - ret[i] for i in range(len(ret) - 1))
