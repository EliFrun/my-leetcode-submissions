# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        out = []
        first_found = False
        def inorder(node):
            nonlocal prev
            nonlocal out
            nonlocal first_found
            if not node:
                return
            inorder(node.left)
            if prev:
                if not first_found and prev.val > node.val:
                    out.append(prev)
                    first_found = True
                if first_found and prev.val > node.val:
                    if len(out) == 2:
                        out.pop()
                    out.append(node)
            prev = node
            inorder(node.right)


        inorder(root)
        tmp = out[0].val
        out[0].val = out[1].val
        out[1].val = tmp

            

        


