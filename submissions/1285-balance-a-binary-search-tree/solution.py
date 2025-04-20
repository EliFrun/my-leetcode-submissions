# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        lis = inorder(root)
        def rebuild(vals):
            if not vals:
                return None
            ret = TreeNode(vals[len(vals)//2])
            ret.left = rebuild(vals[:len(vals)//2])
            ret.right = rebuild(vals[len(vals)//2 + 1:])
            return ret

        return rebuild(lis)

        
