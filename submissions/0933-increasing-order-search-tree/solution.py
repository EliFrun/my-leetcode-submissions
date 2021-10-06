# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inOrder(root):
            if not root:
                return []
            return inOrder(root.left) + [root] + inOrder(root.right)
        
        foo = inOrder(root)
        for i, v in enumerate(foo):
            if i < len(foo) - 1:
                v.left = None
                v.right = foo[i + 1]
            else:
                v.left = None
                v.right = None
            
            
        return foo[0]
