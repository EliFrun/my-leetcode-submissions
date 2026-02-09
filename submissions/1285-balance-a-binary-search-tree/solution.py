# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        in_order = []
        def traverse(curr):
            if not curr:
                return
            traverse(curr.left)
            in_order.append(curr)
            traverse(curr.right)


        def rebuild(l, r):
            if r < l:
                return None
            ret = TreeNode(in_order[(l + r)//2].val)
            ret.left = rebuild(l, (l + r)//2 - 1)
            ret.right = rebuild((l + r)//2 + 1, r)
            return ret

        traverse(root)
        return rebuild(0, len(in_order) - 1)
            

            
        
