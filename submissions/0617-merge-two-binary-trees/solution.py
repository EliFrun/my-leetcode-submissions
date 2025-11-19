# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        ret = TreeNode()

        def traverse(curr, root):
            if not root:
                return
            curr.val += root.val
            if root.left:
                if not curr.left:
                    curr.left = TreeNode()
                traverse(curr.left, root.left)
            if root.right:
                if not curr.right:
                    curr.right = TreeNode()
                traverse(curr.right, root.right)
        traverse(ret, root1)
        traverse(ret, root2)
        return ret
            
